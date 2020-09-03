import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime


import pandas as pd
import numpy

import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

data_1 = pd.read_csv('https://raw.githubusercontent.com/mmasdar/techinasia-dashboard/master/assets/converted_articles.csv', sep=",")


data_1.loc[data_1.parent_categories == 'null']
data_1_1 = data_1.parent_categories.value_counts().tolist()
data_1_11 = data_1.parent_categories.value_counts().index.tolist()

data1 = data_1['total_convert'].head(10)
data2 = data_1['post_title'].head(10)

data1 = list(data1)
data2 = list(data2)


data_1.loc[data_1.child_categories == 'null']
data_1_2 = data_1.child_categories.value_counts().tolist()
data_1_21 = data_1.child_categories.value_counts().index.tolist()


colors = {
    'paper_color': '#393939',
    'text': '#E1E2E5',
    'plot_color': '#ffffff',
    'confirmed_text':'#3CA4FF',
    'deaths_text':'#f44336',
    'recovered_text':'#5A9E6F',
    'highest_case_bg':'#393939',
        }
        
divBorderStyle = {
    'backgroundColor' : '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9,
}
    

tab_3_layout = html.Div([
            html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : data2, 'y' : data1, 'type' : 'bar', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'ARTIKEL PALING BANYAK DIBACA',
                            'legend' : dict(x=0.15, y=0.9)
                        }
                    })
                ], className="row", style={"margin": "1% 3%"}),

        html.Div([
            html.Div([
                html.H4(children='Artikel Terpopuler: ',
                       style={
                           'textAlign': 'center',
                           'color': colors['confirmed_text'],
                       }
                       ),
                html.P(data_1['total_convert'].head(1),
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                    'fontSize': 30,
                }
                ),
                html.P(data_1['post_title'].head(1),
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                }
                ),
            ],
                style=divBorderStyle,
                className='four columns',
            ),
            html.Div([
                html.H4(children='Topik Terpopuler: ',
                       style={
                           'textAlign': 'center',
                           'color': colors['deaths_text'],
                       }
                       ),
                html.P(data_1_1[0],
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                    'fontSize': 30,
                }
                ),
                html.P(data_1_11[0],
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                }
                ),
                html.P(' ', style={'textAlign': 'center', 'color': 'white'}),
            ],
                style=divBorderStyle,
                className='four columns'),
            html.Div([
                html.H4(children='Kategori Terpopuler:',
                       style={
                           'textAlign': 'center',
                           'color': colors['recovered_text'],
                       }
                       ),
                html.P(data_1_2[0],
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                    'fontSize': 30,
                }
                ),
                html.P(data_1_21[0],
                       style={
                    'textAlign': 'center',
                    'color': 'white',
                }
                ),
                html.P(' ', style={'textAlign': 'center', 'color': 'white'}),
            ],
                style=divBorderStyle,
                className='four columns'),
        ], className='row', style={"margin": "2% 3%"}),



            html.Div([
                html.Div([
                    html.H6('Topik Artikel', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                        id='tab_baru_1',
                        figure={
                            'data': [
                            {'x' : data_1_11, 'y' : data_1_1, 'type' : 'bar', 'marker' : {'color' : colors['deaths_text']}},
                            ],
                            'layout': {
                                        'plot_bgcolor' : colors['paper_color'],
                                        'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']}

                            #'title' : 'Tingkat Kematian Pasien Covid-19'
                            }
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Kategori Artikel', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                        id='tab_baru_2',
                        figure={
                            'data': [
                            {'x' : data_1_21, 'y' : data_1_2, 'type' : 'bar', 'marker' : {'color' : colors['recovered_text']}},
                            ],
                            'layout': {
                                        'plot_bgcolor' : colors['paper_color'],
                                        'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']}

                            #'title' : 'Tingkat Kesembuhan Pasien Covid-19'
                            }
                        }
                    )
                ], className="six columns"),
                ], className="row",style={"margin": "1% 3%"}),

            ], className="row", style={"margin": "2% 3%"})
])



