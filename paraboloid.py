"""
FILENAME: graph.py
DESC: Graph a paraboloid
AUTHORS: Anah Lewi and Angelina Li
DATE: 10/11/17
"""

# -*- coding: utf-8 -*-

import numpy as np

from graph import get_app

def get_z(x, y):
    return x**2 + y**2

xlist = list(np.arange(0.1, 0.9, 0.05))
ylist = xlist
zlist = [[get_z(x, y) for x in xlist] for y in ylist]

if __name__ == "__main__":
    app = get_app("Graph of paraboloid z = x^2 + y^2", xlist, ylist, zlist)
    app.server.run(debug=True)
