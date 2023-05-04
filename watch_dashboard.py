import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output

def df_to_plotly(df):
    return {
        'z' : df['total_time'],
        'x' : df['week'],
        'y' : df['day_name']
    }

df = pd.read_csv('data/activities_dashboard.csv')

activities = ['running', 'cycling', 'star_climbing', ]
df['sport'] = df['sport'].apply(lambda x: x if x in activities else None)
df_weekly_total_time = df.groupby('week').agg({
    'total_time' : 'mean'
}).reset_index()
print(df_weekly_total_time)
work_bar_distance_dif = px.histogram(df, x='work_day', y='total_time', histfunc='avg', color='sport')

weight_loss_line_fig = px.line(df_weekly_total_time, x='week', y='total_time',)

time_map = go.Figure(data=go.Heatmap(df_to_plotly(df), colorscale=px.colors.sequential.Greens, ))


app = JupyterDash(__name__)

app.layout = html.Div([
    html.H1('Activity Fitness Dashboard (wip)'),
    dcc.Graph(figure=work_bar_distance_dif),
    dcc.Graph(figure=weight_loss_line_fig),
    dcc.Graph(figure=time_map),
])

if __name__ == '__main__':
    app.run_server()