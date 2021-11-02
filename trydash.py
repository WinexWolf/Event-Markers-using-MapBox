#### Importing all the necessary libraries##########
import numpy as np
import pandas as pd

import seaborn as sns
import plotly
from plotly import __version__
print (__version__)
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import re
import plotly.offline as pyo
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

from datetime import datetime
from datetime import date
import calendar
current_date = date.today()
from io import BytesIO
import base64
from IPython import display
import os
import seaborn as sns
from operator import attrgetter
import matplotlib.colors as mcolors

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_auth

##################

# Reading all the datasets
import datetime
#sets the variable "today" as the datetime object.
today = datetime.datetime.today()
# print (today.strftime('%Y-%m-%d'))
from datetime import datetime, timedelta
last_year= datetime.strftime(datetime.now() - timedelta(3000), '%Y-%m-%d')

#importing requests to access API
import requests
import pandas as pd



#Retrieve data from predict hq api

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash()


app.layout =  html.Div([
html.H1(children='View Events By Selection',style={
    'textAlign': 'center'
}),
html.Hr(),
])

import requests
response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer nW2JOjmghAEdAPzX8cvU6S5MJHNS6bYc7vrlUoJ_",
      "Accept": "application/json"
    },
    params={
        "category" : "sports, academic, community, concerts, conferences, expos, performing-arts, festivals",
        "country":"United Arab Emirates",
        "active.gte": "2021-01-01", "active.lte": "2021-12-31",
        "active.tz":"Asia/Dubai"

    }
)

print(response.json())
import json
with open('data.json', 'w') as outfile:
    json.dump(response.json(), outfile)

import pandas as pd
df=pd.read_json('data.json')
df

df_results=df['results']

from sys import argv
from os.path import exists
import simplejson as json


script, in_file, out_file = argv


data = df['results']

eventdetails = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["location"][0], d["location"][1]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(eventdetails, output)

print (eventdetails)




if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
