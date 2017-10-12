import pandas as pd
import numpy as np
import plotly.plotly as py

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


# Initialize a Dash app
app = dash.Dash()

# We're borrowing the same CSS file used in the Dash tutorial.
app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

