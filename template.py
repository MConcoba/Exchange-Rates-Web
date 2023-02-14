from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html

from dates import date_end, date_start
from request import getData, getSymbols

all_option = []
body = html.Div(
    className='wrapper',
    children=[
        html.H3('Cambio de Modenas a USD', className='main-title'),
        dbc.Row([
            dbc.Col([
                html.Div(
                    className='card',
                    children=[
                        dbc.Label('Ingresa la siguiente informacion',
                                className='card-title'),
                        html.Span("Rango de fechas", className='label'),
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(2023, 1, 1),
                            max_date_allowed=date(
                                date_end.year, date_end.month, date_end.day),
                            initial_visible_month=date(2023, 2, 6),
                            end_date=date(date_end.year, date_end.month, date_end.day),
                            start_date=date(date_start.year,
                                            date_start.month, date_start.day),
                            className='date-picker'
                        ),
                        html.Span("Monedas a consultar", className='label'),
                        dcc.Dropdown(
                            id="country-select",
                            options=getSymbols(),
                            value=['All'],
                            multi=True,
                            style={'margin-bottom':'5px'},
                            placeholder='Selecciona....',

                        ),

                        html.Button('Consultar datos', id='submit',
                                    className='btn btn-primary btn-lg button', n_clicks=0)

                    ]
                ),
            ], width=6),
            dbc.Col([
                html.Div(
                    className='card',
                    children=[
                        dbc.Spinner(children=[html.Div(id='res', className='date-picker', style={'margin': 'auto'})],
                                    size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                    ], style={'align-items': 'center'})
   
            ], width=6)
        ]),
        
       
    ])
