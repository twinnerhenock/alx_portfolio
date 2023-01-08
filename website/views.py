#!/usr/bin/python3

from flask import Blueprint, url_for, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
  
import pandas as pd
import numpy as np
import pickle
import os
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from joblib import load
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.io as pio
pio.kaleido.scope.default_format = "svg"
import joblib

import csv

path = "/home/henock/Documents/alx/portfolio/website"
filepath = os.path.join(path, "df_joined.csv")

with open(filepath) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    values = list(reader)
def column(matrix, i):
    return [row[i] for row in matrix]
columns = ('Year', 'Month', 'week_no', 'Date_no', 'Day', 'holidays', 'traffic')
lst = column(values,0)[1:]
lst2 = column(values,3)[1:]
lst3 = column(values,5)[1:]
lst4 = column(values,4)[1:]
lst5 = column(values,1)[1:]
lst6 = column(values,2)[1:]
lst7 = column(values,2)[1:]
df = pd.DataFrame(list(zip(lst,lst2,lst3,lst4,lst5,lst6,lst7)), columns=columns)

def read_from_tf(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield tf.load_weights('saved_model')
        except EOFError:
            pass

model_path = 'website/ml_model/LSTM_Multivariate'

Trained_model = tf.keras.models.load_model(model_path)

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def gen_picture():
    if request.method == 'POST':
        text = request.form.get('text')
        
        user_params = params_int(text)
        lstm_pred(df, Trained_model, user_params)
    return render_template("home.html", href='static/image.svg',user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

def lstm_pred(df, Trained_model, user_params):

    def data_prep(dataset, target, start, end, window, horizon):
        X = []
        y = []
        start = start + window
        if end is None:
            end = len(dataset) - horizon

        for i in range(start, end, 30):
            indices = range(i-window, i)
            X.append(dataset[indices])

            indicey = range(i+1, i+1+horizon)
            y.append(target[indicey])
        return np.array(X), np.array(y)
    x_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()
    BATCH_SIZE = 16

    dataX = x_scaler.fit_transform(df[['Year', 'Month', 'week_no', 'Date_no', 'Day', 'holidays','traffic']])
    dataY = y_scaler.fit_transform(df[['traffic']])
    hist_window = 360
    horizon = user_params
    TRAIN_SPLIT = 2300
    x_train_multi, y_train_multi = data_prep(
    dataX, dataY, 0, TRAIN_SPLIT, hist_window, horizon)
    x_val_multi, y_val_multi= data_prep(
    dataX, dataY, TRAIN_SPLIT, None, hist_window, horizon)
    validate = df[['Year', 'Month', 'week_no', 'Date_no', 'Day',
    'holidays','traffic']].tail(user_params)
    val_rescaled = x_val_multi.reshape(-1, x_val_multi.shape[1], x_val_multi.shape[2])
  
     
    Predicted_results = Trained_model.predict(val_rescaled)
    Predicted_results_Inv_trans = y_scaler.inverse_transform(Predicted_results)
    fig = px.line(x=validate.index,y=Predicted_results_Inv_trans[0])
    
    
    fig.update_layout(
            title_text = "ETRE's Six-month Traffic Flow Prediction",
            xaxis_title_text = 'Forecast Period(January-June, 2022)',
            yaxis_title_text = 'Traffic Volume')
    fig.show()
    ppath = "website/static/image.svg"
    pio.write_image(fig,ppath, width=600, engine='kaleido')

def params_int(user_params):
    '''Checks if an **input** is
    a positive Integer AND in a specific range'''
    maxValue = 360
    while True:
        try:
           intTarget = int(user_params)
        except ValueError:
            continue
        else:
            if intTarget < 1 or intTarget > maxValue:
                continue
            else:
                return (intTarget)
        return user_params
