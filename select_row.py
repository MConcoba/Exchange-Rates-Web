import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, dash_table, dash
import pandas as pd


app = dash.Dash(__name__)

data = [{'index': i, 'id': i+1, 'date': '2021-01-{:02d}'.format(i+1),
         'ios': 'USD', 'country': 'United States', 'value': i*100} for i in range(100)]

def table_hash(data):
    df = pd.DataFrame(data)

    return html.Div([
        html.Div([
            dbc.Label('Tabla Hash', className='card-title'),
        ]),
        html.Div([
            dbc.Input(id='search-input', type='number', placeholder='Buscar por ID'),
            html.Button('Buscar', id='search-button', n_clicks=0),
            dash_table.DataTable(
                id='table',
                columns=[{"name": 'Index', "id": 'index'}, {"name": 'ID', "id": 'id'},
                         {"name": 'Fecha', "id": 'date'}, {"name": 'Moneda', "id": 'ios'},
                         {"name": 'Nombre Moneda', "id": 'country'}, {"name": 'Valor', "id": 'value'}, ],
                data=df.to_dict('records'),
                style_table={
                    'maxHeight': '80ex',
                    'overflowY': 'scroll',
                    'width': '100%',
                    'minWidth': '100%',
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
            ),
        ], className='', style={'width': '90%', 'margin': 'auto'}
        )
    ])

# Función de devolución de llamada para el evento de selección de fila
@app.callback(
    Output('table', 'page_current'),
    Input('table', 'selected_rows')
)
def scroll_to_selected_row(selected_rows):
    if selected_rows:
        print(selected_rows)
        return int(selected_rows[0] / 100)

# Función de devolución de llamada para la búsqueda de un ID
@app.callback(
    Output('table', 'selected_rows'),
    Input('search-button', 'n_clicks'),
    State('search-input', 'value')
)
def select_row_by_id(n_clicks, id_value):
    if id_value:
        df = pd.DataFrame(data)
        selected_row = df.loc[df['id'] == id_value]

        # Si se encontró una fila, devolver el índice de la fila seleccionada
        if not selected_row.empty:
            row_index = selected_row.index[0]
            return [row_index]

    # Si no se encontró ninguna fila, no seleccionar ninguna fila
    return []

# Ejecutar la aplicación
if __name__ == '__main__':
    app.layout = table_hash(data)
    app.run_server(debug=True)

