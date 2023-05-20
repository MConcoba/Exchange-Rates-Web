import dash_bootstrap_components as dbc
from dash import ctx, State, dash, html, dcc
from dash.dependencies import Input, Output
import dash_interactive_graphviz


app = dash.Dash(__name__, title='Exchange Rates',
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, ])

from controllers.avl_tree import AVLTree



def grafo(datos):
    avl_tree = AVLTree()
    root = None
    for i in datos:
        root = avl_tree.insert(root, i)

    one = avl_tree.get_dots(root, 1, "Se ingresa [2, 1, 3]")
    #print(one)
    graph = """
        digraph {
        subgraph cluster_1 { """ + one + """}
    }
    """
    dcc.Store(id='tr'),

    return dash_interactive_graphviz.DashInteractiveGraphviz(
            id="a",
            dot_source=graph,
            engine="dot",
            style={'height': '80%', 'width': '45%'},  # para limitar el tamaño del contenedor
        ),
    



tow = """
    subgraph cluster_2 {
        label="Se ingresa [5, 4]"
        21 [label = "1"]
        22 [label = "2"]
        23 [label = "3"]
        24 [label = "4"]
        25 [label = "5"]

        22 -> 21
        22 -> 23
        23 -> 25
        25 -> 24
    }
"""

three = """
    subgraph cluster_3 {
        label="Se valancea el arbol"
        31 [label = "1"]
        32 [label = "2"]
        33 [label = "3"]
        34 [label = "4"]
        35 [label = "5"]

        32 -> 31
        32 -> 34
        34 -> 33
        34 -> 35
    }
"""


    

arboles = html.Div([
                    dbc.Row([

                        dbc.Col([
                            html.Div(
                                className='card',
                                children=[
                                    html.Div(className='text-end',
                                             children=[html.Button('Siguiente', id='reload',
                                        className='btn btn-info btn-lg button', n_clicks=0),], style={'width': '90%'}
                                             ),

                                    dbc.Spinner(children = [
                                        html.Div(id='tree-avl', className='date-picker', style={'margin': 'auto', 'minHeight': '535px'})
                                    ],size="lg", color="primary", type="border", fullscreen=True, spinner_style={'margin': 'auto'}),
                                    
                                   
                                ], 
                                
                                style={'alignItems': 'center'})

                        ], width=6)
                    ]),

                ])



# Definir layout de la aplicación
app.layout = arboles

@app.callback(
    [Output('tree-avl', 'children')],
    [Input('reload', 'n_clicks')],
)
def update_output(btn):
    datos = [2, 1, 3, 4, 5]
    arbol = grafo(datos[:3])
   # print('h')
    if 'reload' == ctx.triggered_id:
        pass
    return [arbol]


if __name__ == '__main__':
    app.run_server(debug=True)
