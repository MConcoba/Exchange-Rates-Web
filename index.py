import dash_bootstrap_components as dbc
from dash import Dash, ctx, dash_table, dcc, html
from dash.dependencies import Input, Output, State

from request import find_currencies_labels, getData, getSymbols
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
        if (len(select) > 3):
            s = ",".join(select)
        # find_currencies_labels(getSymbols(), s)
        data = getData(start_date, end_date, s)
        info = 'Revisa la consola'
    else:
        info = 'Para obtener los datos da completa la informacion y da click en el boton'
    return info


if __name__ == '__main__':
    app.run_server(debug=True)
