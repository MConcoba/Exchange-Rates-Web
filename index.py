import dash_bootstrap_components as dbc
from dash import Dash, ctx
from dash.dependencies import Input, Output

from env import prod
from request import getData
from table import table_Data
from template import body

app = Dash(__name__, title='Exchange Rates',
           external_stylesheets=[dbc.themes.BOOTSTRAP])
app._favicon = ("ico.png")
app.layout = body


@app.callback(
    Output('res', 'children'),
    [Input('submit', 'n_clicks'),
     Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('country-select', 'value')],
)
#
def update_output(btn, start_date, end_date, select):
    if 'submit' == ctx.triggered_id:
        s = select
        rows = 1
        if (type(select) == list):
            s = ",".join(select)
            rows = len(select)
        # find_currencies_labels(getSymbols(), s)
        data = getData(start_date, end_date, s)
        #info = 'Revisa la consola 💻'
        info = table_Data(data, rows)
    else:
        info = 'Para obtener los datos da completa la informacion y da click en el boton'
    return info


if __name__ == '__main__':
    app.run_server(debug=prod)
