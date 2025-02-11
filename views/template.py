from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html

from models.dates import date_end, date_start, today
from controllers.request import getSymbols

all_option = []

body = html.Div(
    className='wrapper',
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
        ]),
        dbc.Tabs([
            dbc.Tab(label='Datos', children=[
                dbc.Row([
                    dbc.Col([
                        html.Div(
                            className='card',
                            children=[
                                dbc.Label('Ingresa la siguiente informacion',
                                          className='card-title'),
                                html.Span("Rango de fechas",
                                          className='label'),
                                dcc.DatePickerRange(
                                    id='my-date-picker-range',
                                    min_date_allowed=date(2023, 1, 1),
                                    max_date_allowed=date(
                                        today.year, today.month, today.day),
                                    initial_visible_month=date(
                                        today.year, today.month, today.day),
                                    end_date=date(
                                        date_end.year, date_end.month, date_end.day),
                                    start_date=date(date_start.year,
                                                    date_start.month, date_start.day),
                                    className='date-picker'
                                ),
                                html.Span("Monedas a consultar",
                                          className='label'),
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
                        html.Div(
                            className='card',
                            children=[
                                dbc.Spinner(children=[html.Div(id='res', className='date-picker', style={'margin': 'auto'})],
                                            size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                            ], style={'alignItems': 'center'})

                    ], width=8)
                ]),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Error"),
                        dbc.ModalBody("Ocurrió un error"),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Cerrar", id="error-modal-close", className="ml-auto")
                        ),
                    ],
                    id="error-modal",
                    centered=True,
                    is_open=False,
                )
            ]),
            dbc.Tab(label='', children=[
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                className='card',
                                children=[
                                    dbc.Label('Generar listado aleatorio',
                                              className='card-title'),
                                    html.Span("",
                                              className='label'),
                                    html.Button('Obtener datos', id='random',
                                                className='btn btn-primary btn-lg button', n_clicks=0)

                                ]
                            ),
                        ], width=4),
                        dbc.Col([
                            html.Div(
                                className='card',
                                children=[
                                    dbc.Spinner(children=[html.Div(id='tree', className='date-picker', style={'margin': 'auto'})],
                                                size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                                ], style={'alignItems': 'center'})

                        ], width=8)
                    ]),

                ])
            ])
        ])
    ])
