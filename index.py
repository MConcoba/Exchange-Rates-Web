import dash_bootstrap_components as dbc
from dash import ctx, State, dash, html
from dash.dependencies import Input, Output

from env import prod
from controllers.request import getData
from views.table import table_Data
from views.table_hash import table_hash
from views.tree import binary_tree, avl_tree
from views.template import body
from views.menu import layout_arboles, layout_datos
from views.alert import get_error_modal
from config_dash import app
from controllers.avl_tree import AVLTree
from controllers.table_hash import HashTable

avl_trees = AVLTree()
root = None
hash_table = HashTable(20)


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
    [Output('res', 'children'), Output('tree', 'children'), 
     Output('tree-avl', 'children'), Output('ids-f', 'data'), 
     Output('hash', 'children'), Output('table', 'style_data_conditional'),
    Output('table', 'selected_rows'),],
    [Input('submit', 'n_clicks'),
     Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('country-select', 'value'), Input('reload', 'n_clicks'), 
     Input('search', 'n_clicks')],
     [State('ids-f', 'data'), State('input', 'value')]
)
def update_output(btn, start_date, end_date, select, reload, serach, data, input_value):
    ids = []
    if 'submit' == ctx.triggered_id:
        s = select
        rows = 1
        if (type(select) == list):
            s = ",".join(select)
            rows = len(select)
        datos = getData(start_date, end_date, s)
        if datos['status'] == False:
            return get_error_modal(datos['message'])
        else:
            total_size = 5 * rows + 5
            info = table_Data(datos['records'], rows)
            t = binary_tree(datos['tree'])
            avl = avl_tree(datos['tree'])
            #hash_table.resize(total_size)
            hash_table.clear()
            for item in datos['records']:
                for m in item['monedas']:
                    moneda = {
                        'id': m['id'],
                        'date': item['fecha'],
                        'iso': m['iso'],
                        'country': m['pais'],
                        'value': m['valor']
                    }
                    hash_table.insert(moneda)
            h = table_hash(hash_table.getAll())
            ids = [info, t, avl, datos['ids'], datos['records'], h]
            rows = [{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},{'if': {'state': 'selected'}, 'backgroundColor': 'rgba(0, 0, 0, 0)'}]
            ih =  []
    elif 'reload' == ctx.triggered_id:
       pass
    elif 'search' == ctx.triggered_id:
        highlight_style = {'backgroundColor': '#ffcccb'}

        if input_value:
        # Busca el índice de la fila que contiene el ID coincidente
            #hash_table.search()#print(hash_table.getAll())
            new_list = [elem for elem in hash_table.getAll() if "id" in elem]
            posicion = next((i for i, d in enumerate(new_list) if d.get('id') == int(input_value)), None)
            sear = hash_table.search(new_list[int(posicion)]) 
                # Devuelve un estilo que resalta la fila con el ID coincidente
            rows = {'if': {'row_index': int(sear['index'])}, 'backgroundColor': highlight_style['backgroundColor']},
            ih = [int(sear['index'])]
            datos = {}

            info = data[0]
            t = data[1]
            avl = data[2]
            datos['ids'] = data[3]
            datos['records'] = data[4]
            h = data[5]
            ids = [info, t, avl, datos['ids'], datos['records'], h]
    else:
        return dash.no_update
        info = 'Para obtener los datos da completa la informacion y da click en el boton'
        
    return info, t, avl, ids, h, rows, ih


@app.callback(
    Output("error-modal", "is_open"),
    [Input("error-modal-close", "n_clicks")],
    [State("error-modal", "is_open")],
)
def toggle_error_modal(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


@app.callback(
    Output('table', 'style_table'),
    Input('table', 'selected_rows')
)
def scroll_to_selected_row(selected_rows):

    if selected_rows:
        print('row slected')
        return {'scrollToRow': selected_rows[0]}
    else:
        print('nada selected')
        return dash.no_update



""" @app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):
    if(pathname == '/binary'):
        return layout_arboles
    elif(pathname == '/'):
        return layout_datos
 """
if __name__ == '__main__':
    app.run_server(debug=prod)
