import dash_bootstrap_components as dbc
from dash import dcc, html


def table_Data(data, span):
    rows = []
    for row in data:
        fecha = row['fecha']
        is_first_row = True
        for moneda in row['monedas']:
            iso = moneda['iso']
            pais = moneda['pais']
            valor = moneda['valor']
            if is_first_row:  # si es la primera fila con esa fecha
                rows.append(html.Tr([
                    html.Td(fecha, rowSpan=span, style={
                            'vertical-align': 'middle'}),
                    html.Td(iso),
                    html.Td(pais),
                    html.Td(round(valor, 2))
                ]))
                is_first_row = False  # marcar como que ya no es la primera fila con esa fecha
            else:
                rows.append(html.Tr([
                    html.Td(iso),
                    html.Td(pais),
                    html.Td(round(valor, 2))
                ]))
        
    return html.Div([
        html.Div([
            html.Table([
                html.Thead([
                    html.Tr([
                        html.Th('Fecha', style={'width': '25px'}),
                        html.Th('Moneda'),
                        html.Th('Nombre Moneda'),
                        html.Th('Valor')
                    ])
                ]),
                html.Tbody(rows)
            ], className='table table-bordered table-primary table-striped text-center border border-dark', 
            style={'width': '90%', 'margin': 'auto'})
        ])
    ])
