import dash_bootstrap_components as dbc
from dash import dcc, html
from views.formulario import formulario, binary


sidebar_global = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Datos", href="/", active="exact")),
                dbc.NavItem(dbc.NavLink("Arboles", href="/binary",  active="exact")),
            ],
            pills=True,
        )
    ]
)

layout_datos = html.Div([
    formulario
])

layout_arboles = html.Div([
    binary
])

body_global = html.Div(id="page-content", children=[])

menu = html.Div([dcc.Location(id="url"), sidebar_global, body_global])

