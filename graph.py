"""
FILENAME: graph.py
DESC: Create a simple graph on an x-y-z plane, as done in the demo.
AUTHORS: Anah Lewi and Angelina Li
DATE: 10/11/17
"""

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


"""
DATA:
* x: student_id
* y: date
* z: waste percentage
"""

df = pd.read_csv("new_food_obs.csv")
df["day"] = df["date"].apply(lambda string: int(string.split("/")[1]))
del df["date"]

df = df.pivot(
    index="day", columns="SID", values="waste?")

xlist = list(df.columns)
ylist = list(df.index)
zlist = df.values.tolist()

"""
FUNCTIONS:
"""

def get_figure(fig_title, xlist, ylist, zlist):
    trace1 = dict(
        type="surface",
        x=xlist,
        y=ylist,
        z=zlist,
        hoverinfo="x+y+z",
        lighting={
            "ambient": 0.95,
            "diffuse": 0.99,
            "fresnel": 0.01,
            "roughness": 0.01,
            "specular": 0.01,
        },
        opacity=0.7,
        showscale=False,
        scene="scene"
    )

    trace2 = dict(
        type="scatter3d",
        mode="lines",
        x=xlist,
        y=ylist,
        z=zlist,
        hoverinfo="x+y+z",
        line=dict(color="#444444")
    )

    data = [trace1, trace2]

    layout = go.Layout(
        title=fig_title,
        autosize=True,
        font=dict(
            size=12,
            color="#CCCCCC",
        ),
        margin=dict(
            t=30,
            l=20,
            b=20,
            r=20
        ),
        showlegend=False,
        hovermode="closest",
        scene=dict(
            aspectmode="manual",
            xaxis={
                "showgrid": True,
                "title": "",
                "type": "category",
                "zeroline": False,
                "categoryorder": "array",
                "categoryorder": xlist[::-1]
            },
            yaxis={
                "showgrid": True,
                "title": "",
                "zeroline": False
            },
            zaxis={
                "title": ""
            }
        )
    )

    return dict(data=data, layout=layout)


def get_app(fig_title, xlist, ylist, zlist):
    app = dash.Dash()

    # We're borrowing the same CSS file used in the Dash tutorial.
    app.css.append_css({
        'external_url': (
            'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
            '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
        )
    })

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
        # body
        html.Div(
            [
                dcc.Graph(
                    id="graph",
                    figure=get_figure(fig_title, xlist, ylist, zlist),
                    style={"height": "80vh"}
                )
            ],
            id="page"
        )
    ])

    return app


if __name__ == "__main__":
    app = get_app("Food waste per student over time", xlist, ylist, zlist)
    app.server.run(debug=True)
