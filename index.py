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



)
def update_output(btn, start_date, end_date,):
    print(btn)
    if btn > 0:
        data = getData(start_date, end_date)
        info = 'Revisa la consola'
    else:
        info = 'Para obtener los datos da click en el boton de arriba'

    return info


if __name__ == '__main__':
    app.run_server(debug=True)
