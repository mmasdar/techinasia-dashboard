import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from operator import attrgetter
import matplotlib.colors as mcolors
plt.style.use('seaborn')

import dash
import base64
import dash_html_components as html


test_png = 'Cohort-Analysis.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

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

                  html.Img(src='data:image/png;base64,{}'.format(test_base64), height=1000),
                  #html.Div(html.Img(src=app.get_asset_url('logo.png'), style={'height':'10%', 'width':'10%'}))

                ], className="row", style={"margin": "1% 3%"}),

            ], className="row", style={"margin": "1% 3%"})
])



