import dash_bootstrap_components as dbc
from dash import Dash, ctx, dash_table, dcc, html

from template import body

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = body

if __name__ == '__main__':
    app.run_server(debug=True)
