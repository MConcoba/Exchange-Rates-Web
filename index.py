import dash_bootstrap_components as dbc
from dash import ctx, State, dash, html
from dash.dependencies import Input, Output

from env import prod
from controllers.request import getData
from views.table import table_Data
from views.tree import binary_tree
from views.data import datos
from views.template import body
from views.alert import get_error_modal
from config_dash import app

""" @app.callback(
    Output("page-tree", "children"),
    [Input("url-tree", "pathname")]
)
def render_page_content(pathG):
    print(pathG)
    if pathG == "/binary":
        return show_tree
    elif pathG == '/avl':
        return show_tree """

@app.callback(
    [Output('res', 'children'), Output('tree', 'children'), ],
    [Input('submit', 'n_clicks'),
     Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('country-select', 'value'), Input("url-tree", "pathname")],
)
def update_output(btn, start_date, end_date, select, path):
    if 'submit' == ctx.triggered_id:
        s = select
        rows = 1
        if (type(select) == list):
            s = ",".join(select)
            rows = len(select)
        data = getData(start_date, end_date, s)
        if data['status'] == False:
            return get_error_modal(data['message'])
        else:
            info = table_Data(data['records'], rows)
            t = binary_tree(data['tree'], data['tooltips'])
    else:
        return dash.no_update
        info = 'Para obtener los datos da completa la informacion y da click en el boton'
    return info, t


@app.callback(
    Output("error-modal", "is_open"),
    [Input("error-modal-close", "n_clicks")],
    [State("error-modal", "is_open")],
)
def toggle_error_modal(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=prod)
