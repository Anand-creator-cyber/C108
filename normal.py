import pandas as pd 
import plotly.express as px
import csv 
import plotly.figure_factory as ff

df = pd.read_csv(r"C:\Users\91814\OneDrive\Desktop\Whitehat\Class 108\dt.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist = False)
fig.show()
