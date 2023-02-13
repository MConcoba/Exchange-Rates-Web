from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html

from dates import date_end, date_start

body = html.Div(
    className='wrapper',
    children=[
        html.H3('Cambio de Modenas a USD', className='main-title'),
        html.P('En rango de fechas', className='paragraph-lead'),
        html.Div(
            className='card',
            children=[
                html.H3('Seleccionar el rango de fecha',
                        className='card-title'),
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
                html.Button('Consultar datos', id='submit',
                            className='btn btn-primary btn-lg button', n_clicks=0)

            ]
        ),
        html.Div(
            className='card',
            children=[
                dbc.Spinner(color="primary", type="grow",
                            id="loading-indicator", spinnerClassName='loader'),
                html.Div(id='res', className='date-picker')
            ])
    ])
