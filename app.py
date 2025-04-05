import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("spy_data.csv", names=["timestamp", "price"], parse_dates=["timestamp"])

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("📈 SPY Dashboard"),
    
    dcc.Graph(
        id='spy-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['timestamp'],
                    y=df['price'],
                    mode='lines+markers',
                    name='SPY Price'
                )
            ],
            'layout': {
                'title': 'Évolution du prix du SPY'
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)

