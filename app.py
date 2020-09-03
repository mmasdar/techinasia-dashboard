import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from assets import global_tab, asia_tenggara_tab, indonesia_tab

import pandas as pd
import plotly.figure_factory as ff
import numpy as np

import plotly.graph_objs as go
import datetime


external_stylesheets = ["static/css/style.css", 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {"background": "#2D2D2D", "background_div": "white", 'text': 'white'}

app.config['suppress_callback_exceptions']= True

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('DASHBOARD DATA', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Div([html.Span('Analisis Reader Behavior in Techinasia Indonesia by Muhammad Masdar Mahasin (2020)',
                             style={'color': colors['text'],
                             })
                        ], style={'textAlign' : 'center'}),


    dcc.Tabs(id="tabs", className="row", style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='data', children=[
        dcc.Tab(label='Analisis Data 1', value='data'),
        dcc.Tab(label='Cohort Analysis', value='dem_tab'),
        dcc.Tab(label='Indonesia', value='med_tab')
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])


def render_content(tab):
    if tab == 'dem_tab'     :
        return asia_tenggara_tab.tab_3_layout
    elif tab == 'med_tab'   :
        return indonesia_tab.tab_3_layout
    elif tab == 'data'      :
        return global_tab.tab_3_layout


if __name__ == "__main__":
    app.run_server(debug=True)