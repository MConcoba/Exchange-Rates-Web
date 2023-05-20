import dash_bootstrap_components as dbc
from dash import html, dash_table
import pandas as pd
import dash_tabulator
from dash_iconify import DashIconify
import pickle



def table_hash(data):
    df = pd.DataFrame(data)
    clearFilterButtonType = {"css": "btn btn-outline-dark", "text": "Clear Filters"}

    return html.Div([
        html.Div([
            dbc.Label('Tabla Hash', className='card-title'),
        ]),
        html.Div([
            dash_table.DataTable(
                id='table',
                columns=[{"name": 'Index', "id": 'index'}, {"name": 'ID', "id": 'id'},
                         {"name": 'Fecha', "id": 'date'}, {"name": 'Moneda', "id": 'iso'},
                         {"name": 'Nombre Moneda', "id": 'country'}, {"name": 'Valor', "id": 'value'}, ],
                data=df.to_dict('records'),
                fixed_rows={'headers': True, 'data': 0},
                style_table={
                'maxHeight': '80ex',
                'width': '100%',
                'minWidth': '100%',
                'overflowY': 'hidden !important'

                },
                # style cell
                style_cell={
                    'fontFamily': 'Open Sans',
                    'textAlign': 'center',
                    'height': '60px',
                    'padding': '2px 22px',
                    'whiteSpace': 'inherit',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                },
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'State'},
                        'textAlign': 'left'
                    },
                ],
                # style header
                style_header={
                    'fontWeight': 'bold',
                    'backgroundColor': 'white',
                },
                style_data_conditional=[
                    # Estilo predeterminado para las filas
                    {'if': {'row_index': 'odd'}, 
                     'backgroundColor': 'rgb(248, 248, 248)',
                    },
                    # Estilo para las filas resaltadas
                    {'if': {'state': 'selected'}, 
                     'backgroundColor': 'rgba(0, 0, 0, 0)',
                    },
                
                ],
                
                # Permite la selección de filas
                row_selectable='single',
                selected_rows=[],

                filter_action="native",
                sort_action="native",
            ),
            
        ], className='',
                style={'width': '90%', 'margin': 'auto'}
        )
    ])
