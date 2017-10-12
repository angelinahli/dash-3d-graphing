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


# app's layout specifies what should appear where.
# creating a very simple layout to test things out.

app.layout = html.Div([
    
    # Title
    html.Div(
        [
            dcc.Markdown(
                """
                ### Testing out the NYTimes Yield Curve App
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

    # slider that comes with 3 components:
    # (1) slider with no labels that allows user to access different panes
    # (2) two buttons --> back and forwards, for better navigation between panes
    # (3) text that is read in from 
    html.Div(
        [
            # simple slider with 4 panes to flick through.
            html.Div(
                [
                    dcc.Slider(
                        min=0,
                        max=3,
                        value=3,
                        marks={i: '' for i in range(4)},
                        id="slider"
                    )
                ],
                className="row",
                style={"margin-bottom": "10px"}
            ),

            # pane displaying both the buttons and the text associated with each pane
            html.Div(
                [
                    # back and forward buttons
                    # NOTE: calling these ids "backwards" and "forwards" to
                    # demonstrate we get how to use ids.
                    html.Div(
                        [
                            # backwards button first
                            html.Button("Back", id="backwards", style={
                                    "display": "inline-block"
                                }),
                            # forwards button next
                            html.Button("Next", id="forwards", style={
                                    "display": "inline-block"
                                })
                        ],
                        className="two columns offset-by-two"
                    ),

                    # text associated with each pane
                    dcc.Markdown(
                        id="text",
                        className="six columns"
                    ),
                ],
                className="row",
                style={"margin-bottom": "10px"}
            ),

            # the actual graph we want comes next (where precisely this is
            # positioned is, we assume, specified by our css file)
            dcc.Graph(
                id="graph",
                style={"height": "65vh"}
            ),
        ],
        id="page"
    ),
])