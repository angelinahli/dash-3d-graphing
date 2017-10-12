"""
FILENAME: slider.py
DESC: Demonstrate the functionality of the sliders used in the demo.
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
PART 2: Define some internal data we will rely on later.
"""

# specifies how many panes we want to appear.
NUM_PANES = 4

# contains a markdown string description for each pane.
TEXTS = {
    i: """
    \n\n
    #### Pane {i} title
    Here is some sample text for pane number {i}. We can use this space to
    describe what this pane consists of.
    """.format(i=i + 1).replace("  ", "") for i in range(0, NUM_PANES)
}

# initialize these to 0 beforehand
last_back_val = 0
last_next_val = 0


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
                ## Dash Demonstrations: Different panes
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

    # Slider with different labels associated with each pane.
    html.Div(
        [
            # simple slider with 4 panes to flick through.
            html.Div(
                [
                    dcc.Slider(
                        min=0,
                        max=3,
                        value=3,
                        marks={i: 'Pane {}'.format(i + 1) for i in range(4)},
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
            )
        ],
        id="page"
    ),
])


"""
PART 4: Create the different components of our app
"""

@app.callback(Output("text", "children"), [Input("slider", "value")])
def make_text(value):
    """
    Returns text labels given each pane view we have.
    callback will assign this text output to the dcc Markdown obj we created in
    layout (i.e. this text will be used to create descriptions of each pane)
    
    Output text: the text the markdown obj we defined above takes on.

    Input slider: the whole slider obj defined above
    Input value: value the slider is resting on right now.
    """

    # if for some reason value is none, shift back to the first pane.
    if value is None:
        value = 0

    return TEXTS[value]

@app.callback(
    Output("slider", "value"),
    [
        Input("backwards", "n_clicks"),
        Input("forwards", "n_clicks"),
    ],
    [State("slider", "value")])
def move_slider(back_val, next_val, slider):
    """
    Sets the value of each element.
    Here, backwards id corresponds with back_val parameter;
    forwards id corresponds with next_val parameter;
    state of slider corresponds with slider parameter.
    """

    # if any of these elements have no value coming in, set them to 0
    if back_val is None:
        back_val = 0
    if next_val is None:
        next_val = 0
    if slider is None:
        slider = 0

    global last_back_val
    global last_next_val

    # return either minimum pane index or one index back.
    if back_val > last_back_val:
        last_back_val = back_val
        return max(0, slider - 1)

    # return either maximum pane index or one index forwards.
    if next_val > last_next_val:
        last_next_val = next_val
        return min(NUM_PANES - 1, slider + 1)


"""
PART 5: Run the Dash app
"""

if __name__ == "__main__":
    app.server.run(debug=True)