import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.H1("SPY Dashboard - Initial layout")

if __name__ == '__main__':
    app.run(debug=True)
