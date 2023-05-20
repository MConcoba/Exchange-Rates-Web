import dash_bootstrap_components as dbc
from dash import Dash
from dash import dcc, html
from views.template import body
from views.menu import menu
from views.tabs import tabs
from views.header import encabezado
from views.error_modal import modal
from views.formulario import formulario, binary, avl




app = Dash(__name__, title='Exchange Rates',
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, ])
app._favicon = ("ico.png")
#app.layout = html.Div([header, menu])
app.layout =  html.Div(className='wrapper', children=[encabezado, tabs(formulario, binary, avl), modal])