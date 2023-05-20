
import dash_bootstrap_components as dbc
from dash import html


encabezado = html.Div(
    children=[
        dbc.Row([
            dbc.Col([
                html.Div(children=[
                    html.Img(src='assets/ico.png'),
                    html.H3('Cambio de Modenas a USD', className='main-title',
                            style={'margin': 'auto 5px'}),
                ], style={'display': 'flex', 'margin': 'auto',
                          'justifyContent': 'center'})
            ])
        ]),])