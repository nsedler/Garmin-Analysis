import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data/garmin_activities.csv')

fig = go.Figure(data=[go.Table(
    header = dict(values=list(df.columns)),
    cells = dict(values=df.transpose().values.tolist())
)])

fig.show()