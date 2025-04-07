import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
import os

app = dash.Dash(__name__)

def load_data():
    try:
        df = pd.read_csv("spy_data.csv", names=["timestamp", "price"], parse_dates=["timestamp"])
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "price"])

def load_report():
    try:
        with open("daily_report.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "🕗 Rapport journalier non encore généré. Il sera mis à jour à 20h."

app.layout = html.Div(children=[
    html.H1("📈 SPY Dashboard"),

    dcc.Graph(id='spy-graph'),

    html.H3("📋 Rapport journalier – mis à jour chaque jour à 20h"),
    html.Pre(id="report", style={"backgroundColor": "#f9f9f9", "padding": "10px", "whiteSpace": "pre-wrap"}),

    # Interval de mise à jour automatique toutes les 5 minutes
    dcc.Interval(
        id='interval-component',
        interval=5 * 60 * 1000,  # en millisecondes
        n_intervals=0
    )
])

@app.callback(
    [dash.dependencies.Output('spy-graph', 'figure'),
     dash.dependencies.Output('report', 'children')],
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    df = load_data()
    report = load_report()

    fig = {
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
    return fig, report

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

