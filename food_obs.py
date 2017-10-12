import numpy as np
import pandas as pd
from pandas import DataFrame

"""
We're plotting:
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

if __name__ == "__main__":
    print xlist
    print ylist
    print zlist

    print df