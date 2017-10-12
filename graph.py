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

from food_obs import xlist, ylist, zlist

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
PART 2: Define the layout of the Dash app
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
PART 3: Create the different components of this app
"""

@app.callback(Output("graph", "figure"))
def make_graph():
    
    trace1 = dict(
        type="surface",
        x=xlist,
        y=ylist,
        z=zlist,
        hoverinfo="x+y+z",
        lighting={
            "ambient": 0.95,
            "diffuse": 0.95,
            "fresnel": 0.05,
            "roughness": 0.05,
            "specular": 0.01
        },
        colorscale=[
            [0, "rgb(255, 237, 237)"],
            [0.25, "rgb(249, 162, 162)"],
            [0.5, "rgb(242, 104, 104)"],
            [0.75, "rgb(242, 77, 77)"],
            [1, "rgb(242, 43, 43)"]
        ],
        opacity=0.7,
        showscale=False,
        zmax=80.0,
        zmin=0.0,
        scene="scene",
    )

