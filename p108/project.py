import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("avg (1).csv")
fig = ff.create_distplot(
    [df["Avg Rating"].to_list()],
    ["Average Rating"],
    show_hist = False
)

fig.show()



























