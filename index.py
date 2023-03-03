import dash_bootstrap_components as dbc
from dash import ctx, State, dash
from dash.dependencies import Input, Output

from env import prod
from controllers.request import getData
from views.table import table_Data
from views.template import body
from views.alert import get_error_modal
from config_dash import app


@app.callback(
    Output('res', 'children'),
    [Input('submit', 'n_clicks'),
     Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('country-select', 'value')],
)

def update_output(btn, start_date, end_date, select):
    if 'submit' == ctx.triggered_id:
        s = select
        rows = 1
        if (type(select) == list):
            s = ",".join(select)
            rows = len(select)
        data = getData(start_date, end_date, s)
        #info = 'Revisa la consola 💻'
        if data['status'] == False:
            return get_error_modal(data['message'])
        else: 
            info = table_Data(data['records'], rows)
    else:
        return dash.no_update
        info = 'Para obtener los datos da completa la informacion y da click en el boton'
    return info

@app.callback(
    Output("error-modal", "is_open"),
    [Input("error-modal-close", "n_clicks")],
    [State("error-modal", "is_open")],
)
def toggle_error_modal(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open



    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    row_index = int(button_id.split('-')[-1])

    # elimina la fila correspondiente de la lista de datos
    del data[row_index]

    # actualiza la tabla con los datos actualizados
    updated_table = table_Data(data)
    
    return updated_table


if __name__ == '__main__':
    app.run_server(debug=prod)
