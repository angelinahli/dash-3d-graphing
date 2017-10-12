import pandas as pd

"""
We're plotting:
* x: student_id
* y: date
* z: waste percentage
"""

df = pd.read_csv("cleaned_food_obs.csv")

xlist = []
ylist = []
zlist = []
for _, data in df.iterrows():
    """
    Only include data for which there are no missing values.
    st20 data is formatted differently and is dropped for the sake of demonstration.
    """
    if (pd.notnull(data[1]) and pd.notnull(data[2]) and 
        pd.notnull(data[13]) and data[1] != "st20"):
        xlist.append(data[1])
        ylist.append(data[2])
        zlist.append(data[13])
