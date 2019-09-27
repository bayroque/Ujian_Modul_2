import plotly
import plotly.express as px
import plotly.graph_objects as go
from cleaning_data import mpg
import json

def dist1():
    df = mpg()
    df_group = df['mpg'].value_counts()
    fig = go.Figure([
        go.Bar(x=df_group.index,y=df_group.values)
    ])
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def dist2():
    df = mpg()
    df_group = df['horsepower'].value_counts()
    fig = go.Figure([
        go.Bar(x=df_group.index,y=df_group.values)
    ])
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
