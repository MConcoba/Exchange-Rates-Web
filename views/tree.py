import dash_bootstrap_components as dbc
from dash import html
import dash_interactive_graphviz


def binary_tree(dots):
    initial_dot_source = """
        digraph { node [style="filled"]  """+  dots + """ } """

    return html.Div([
        html.Div([
            dbc.Label('Arbol Binario', className='card-title'),
        ]),
        dash_interactive_graphviz.DashInteractiveGraphviz(
            id="gv1", 
            dot_source=initial_dot_source, 
            engine="dot",
            style={'height': '80%', 'width': '45%'},  # para limitar el tamaño del contenedor
        ),
    ])


def avl_tree(dots):
    new = """
        digraph { node [style="filled"]  """+  dots + """ } """

    return html.Div([
        dash_interactive_graphviz.DashInteractiveGraphviz(
            id="gv2", 
            dot_source = new, 
            engine="dot",
            style={'height': '80%', 'width': '45%'},  # para limitar el tamaño del contenedor
        ),
    ])


def create_alert():
        return dbc.Alert(
            id="alert",
            color="info",
            is_open=False,
            duration=4000,
            style={"position": "fixed", "top": 0, "right": 0, "width": "20%", "margin": "10px"},
        )
