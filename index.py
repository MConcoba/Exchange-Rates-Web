import dash_bootstrap_components as dbc
from dash import Dash, ctx, dash_table, dcc, html
from dash.dependencies import Input, Output, State

from request import getData
from template import body

app = Dash(__name__, title='Exchange Rates',
           external_stylesheets=[dbc.themes.BOOTSTRAP])
app._favicon = ("ico.png")
app.layout = body


@app.callback(
    Output('res', 'children'),
    [Input('submit', 'n_clicks'),
     Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')],
    [State('loading-indicator', 'spinnerClassName')]
)
def update_output(btn, start_date, end_date, spinnerClassName):
    # Obtener datos de la API
    info = ''
    if start_date is not None:
        info = 'Sin informacion'
    if "submit" == ctx.triggered_id:
        spinnerClassName = "block"
        data = getData(start_date, end_date)

    return info


if __name__ == '__main__':
    app.run_server(debug=True)
