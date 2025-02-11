import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify
import pickle



def table_Data(data, span):
    rows = []
    for row in data:
        fecha = row['fecha']
        is_first_row = True
        for moneda in row['monedas']:
            id = moneda['id']
            iso = moneda['iso']
            id = moneda['id']
            pais = moneda['pais']
            valor = moneda['valor']
            if is_first_row:  # si es la primera fila con esa fecha
                rows.append(html.Tr([
                    html.Td(fecha, rowSpan=span, style={
                            'verticalAlign': 'middle'}),
                    html.Td(id),
                    html.Td(iso),
                    html.Td(pais),
                    html.Td(round(valor, 2)),
                     #html.Td(
                    #    DashIconify(
                    #        icon="ion:trash", color="red", width=30, className="ac-icon"
                    #    )
                    #),
                ]))
                is_first_row = False  # marcar como que ya no es la primera fila con esa fecha
            else:
                rows.append(html.Tr([
                    html.Td(id),
                    html.Td(iso),
                    html.Td(pais),
                    html.Td(round(valor, 2)),
                    #html.Td(
                    #    DashIconify(
                    #        icon="ion:trash", color="red", width=30, className="ac-icon"
                    #    )
                    #),
                ]))

    return html.Div([
        html.Div([
            dbc.Label('Resultados de cambios a USD', className='card-title'),
        ]),
        html.Div([
            html.Table([
                html.Thead([
                    html.Tr([
                        html.Th('Fecha', style={'width': '125px'}),
                        html.Th('Id'),
                        html.Th('Moneda'),
                        html.Th('Nombre Moneda'),
                        html.Th('Valor'),
                       # html.Th('Acciones')
                    ])
                ]),
                html.Tbody(rows)
            ], className='table table-bordered table-primary table-striped text-center border border-dark tabla',
                style={'width': '90%', 'margin': 'auto'})
        ])
    ])
