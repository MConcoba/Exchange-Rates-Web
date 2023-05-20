import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from datetime import date

from models.dates import date_end, date_start, today
from controllers.request import getSymbols


sidebar_trees = html.Div(
    [
        html.H2("", className="display-4"),
        html.Hr(),
        html.P(
            "Tipos de arboles", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Arbol Binario", href="/binary", active="exact"),
                dbc.NavLink("Arbol AVL", href="/avl", active="exact"),
            ],
            vertical=False,
            pills=True,
        ),
    ],
    
)

binary = html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                className='card',
                                children=[
                                    dbc.Spinner(children = [
                                        html.Div(id='tree', className='date-picker', style={'margin': 'auto', 'minHeight': '535px'})
                                    ],size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                                ], style={'alignItems': 'center'})

                        ], width=10, style={'margin': 'auto'}),
                       
                    ]),

                ],)


avl = html.Div([
                    dbc.Row([
                       
                        dbc.Col([
                            html.Div(
                                className='card',
                                children=[
                                    html.Div(className='text-end',
                                             children=[html.Button('Siguiente', id='reload',
                                        className='btn btn-info btn-lg button', n_clicks=0),], style={'width': '90%'}
                                             ),
                                    dcc.Store(id='ids-f'),
                                    dcc.Store(id='tr'),

                                    dbc.Spinner(children = [
                                        html.Div(id='tree-avl', className='date-picker', style={'margin': 'auto', 'minHeight': '535px'})
                                    ],size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                                    
                                   
                                ], 
                                
                                style={'alignItems': 'center'})

                        ], width=10, style={'margin': 'auto'})
                    ]),

                ])



formulario = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div(
                className='card',
                children=[
                    dbc.Label('Ingresa la siguiente informacion', className='card-title'),
                    html.Span("Rango de fechas", className='label'),
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=date(2023, 1, 1),
                        max_date_allowed=date(today.year, today.month, today.day),
                        initial_visible_month=date(today.year, today.month, today.day),
                        end_date=date(date_end.year, date_end.month, date_end.day),
                        start_date=date(date_start.year,date_start.month, date_start.day),
                        className='date-picker'
                    ),
                    html.Span("Monedas a consultar", className='label'),
                    dcc.Dropdown(
                        id="country-select",
                        options=getSymbols(),
                        multi=True,
                        style={'marginBottom': '5px'},
                        placeholder='Selecciona....',
                        value='GTQ'
                    ),
                    html.Button('Consultar datos', id='submit',
                                className='btn btn-primary btn-lg button', n_clicks=0)
                ]
            ),
        ], width=4),
        dbc.Col([
            html.Div(className='card', children=[
                dbc.Spinner(children=[
                    html.Div(id='res', className='datos-tabla', style={'margin': 'auto'})
                ], size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto', }),
            ], style={'alignItems': 'center'}),
        ], width=8),
    ]),


     dbc.Row([
        dbc.Col([
            html.Div(
                className='card',
                children=[
                    dbc.Label('Busqueda en Tabla Hash', className='card-title'),
                    html.Span("ID a buscar", className='label'),
                    dbc.Input(id="input", placeholder="ID...", type="text"),
                    
                    html.Button('Buscar', id='search',
                                className='btn btn-primary btn-lg button', n_clicks=0)
                ]
            ),
        ], width=4),
        dbc.Col([
            html.Div(className='card', children=[
                dbc.Spinner(children=[
                    html.Div(id='hash', className='datos-tabla', style={'margin': 'auto'})
                ], size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto', }),
            ], style={'alignItems': 'center'}),
        ], width=8),
        dash_table.DataTable(id='table')
    ]),
])


