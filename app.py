import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go

# Charger les données de prix
df = pd.read_csv("spy_data.csv", names=["timestamp", "price"], parse_dates=["timestamp"])

# Charger le rapport journalier
try:
    with open("daily_report.txt", "r") as f:
        report_text = f.read()
except FileNotFoundError:
    report_text = "🕗 Rapport journalier non encore généré. Il sera mis à jour à 20h."

# Créer l'app Dash
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
    ),

    html.H3("📋 Rapport journalier – mis à jour chaque jour à 20h"),
    html.Pre(report_text, style={"backgroundColor": "#f9f9f9", "padding": "10px", "whiteSpace": "pre-wrap"})
])

if __name__ == '__main__':
    app.run(debug=True)
