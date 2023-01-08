#!/usr/bin/python3

from website import create_app
from dash_app import create_dash_application

app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True)
