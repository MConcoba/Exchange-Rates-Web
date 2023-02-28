import dash_bootstrap_components as dbc
from dash import Dash
from views.template import body


app = Dash(__name__, title='Exchange Rates',
           external_stylesheets=[dbc.themes.BOOTSTRAP])
app._favicon = ("ico.png")
app.layout = body