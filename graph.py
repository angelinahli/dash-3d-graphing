"""
FILENAME: graph.py
DESC: Create a simple graph on an x-y-z plane, as done in the demo.
AUTHORS: Anah Lewi and Angelina Li
DATE: 10/11/17
"""

import pandas as pd
import numpy as np
import plotly.plotly as py

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html

"""
PART 1: Initialize the app and assign a CSS file.
"""

# Initialize a Dash app
app = dash.Dash()

# We're borrowing the same CSS file used in the Dash tutorial.
app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})


"""
PART 2: Import and manipulate the data we need to create an x-y-z plane graph
"""


"""
PART 3: Define the layout of the Dash app
This just tells elements in our app where they should appear
"""

app.layout = html.Div([
    
    # Title
    html.Div(
        [
            dcc.Markdown(
                """
                ## Dash Demonstrations: 3-D Graphing
                By Angelina Li and Anah Lewi
                """.replace("  ", ""),
                className="eight columns offset-by-two"
            )
        ],

        className="row",
        style={
            "text-align": "center",
            "margin-bottom": "20px"
        }
    ),

    html.Div(
        [
            # the graph will simply exist here!
            dcc.Graph(
                id="graph",
                style={"height": "65vh"}
            ),
        ],
        id="page"
    ),
])

"""
PART 4: Create the different components of this app
"""


