#!/usr/bin/python3

import dash
import dash_core_components as dcc
from dash import Dash, html, dcc, Output, Input, callback
import plotly.express as px
import pandas as pd
from flask_login.utils import login_required
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.io as pio
pio.kaleido.scope.default_format = "svg"
import os
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
lst2 = column(values,1)[1:]
lst3 = column(values,2)[1:]
lst4 = column(values,3)[1:]
lst5 = column(values,4)[1:]
lst6 = column(values,5)[1:]
lst7 = column(values,6)[1:]
df = pd.DataFrame(list(zip(lst,lst2,lst3,lst4,lst5,lst6,lst7)), columns=columns)
filepath2 = os.path.join(path, "daily_tulu_data.csv")

with open(filepath2) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    values = list(reader)
colum = ('V1&V2', 'V3', 'V4', 'V5&V6&V7')
lst = list(map(int,column(values,2)[1:]))
lst2 = list(map(int,column(values,3)[1:]))
lst3 = list(map(int,column(values,4)[1:]))
lst4 = list(map(int,column(values,5)[1:]))
df2 = pd.DataFrame(list(zip(lst,lst2,lst3,lst4)), columns=colum)
value = [sum(list(map(int,column(values,2)[1:]))),sum(list(map(int,column(values,3)[1:]))),
            sum(list(map(int,column(values,4)[1:]))), sum(list(map(int,column(values,5)[1:])))]



def create_dash_application(app):
    dash_app = dash.Dash(
            server=app, name="Dashboard", url_base_pathname='/dash/')
    dash_app.layout = html.Div([

    html.H1(children="Welcome to Ethiopian Toll Roads Enterprise DashBoard"),
    dcc.Dropdown(options=['Pie Chart','Line Chart','Box Plot'], value='Please Select type', clearable=True, id='model'),
    #dcc.RadioItems(options=['day in week', 'day in month', 'month of the year', 'week of the year', 'holiday', 'year'], id='my-radio-btn'),
    dcc.Graph(figure=px.histogram(df, x='Year', y='traffic'), id='fig', clickData={}),
    dcc.Graph(figure={}, id='my_fig')
])
    return dash_app

@callback(
    Output(component_id='fig', component_property='value'),
    Input(component_id='model', component_property='value')
)
def change_pic(chosen_state):
    print(chosen_state)
    print(type(chosen_state))
    if chosen_state == 'Box Plot':
        fig = go.Figure()

        fig.add_trace(go.Box(x=df['Day'].values,y=df['traffic'], name='Day'))
        fig.add_trace(go.Box(x=df['Date_no'].values,y=df['traffic'], name='Date_no'))
        fig.add_trace(go.Box(x=df['Month'].values,y=df['traffic'], name='Month'))
        fig.add_trace(go.Box(x=df['holidays'].values,y=df['traffic'], name='Holidays'))
        fig.update_layout(title_text="ETRE's Traffic Trend")
        return fig.show()
    elif chosen_state == 'Line Chart':
            
        fig = go.Figure([go.Scatter(x=df['Year'], y=df['traffic'])])
        fig.update_xaxes(rangeslider_visible=True)
        return fig.show()
    elif chosen_state == 'Pie Chart':
        fig = px.pie(df2, values=value, names=['Vehicle 1 & Vehicle 2', 'Vehicle 3', 'Vehicle 4', 'Vehicle 5&6&7'])
        return fig.show()
          
    


