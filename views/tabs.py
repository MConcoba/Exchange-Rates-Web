import dash_bootstrap_components as dbc



def tabs(datos, arboles, avl):
    return  dbc.Tabs([
    dbc.Tab(label='Datos', children=[datos]),
    dbc.Tab(label='Arbol-Binario', children=[arboles]),
    dbc.Tab(label='Arbol-AVL', children=[avl])
])