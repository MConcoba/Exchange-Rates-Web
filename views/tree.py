import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify
import dash_interactive_graphviz


def binary_tree(dots, tool):
    tooltip_text = ''.join(tool)

    initial_dot_source = """
        digraph { """ + tooltip_text +  dots + """ } """
    return html.Div(
        dash_interactive_graphviz.DashInteractiveGraphviz(
            id="gv1", 
            dot_source=initial_dot_source, 
            engine="dot",
            style={'height': '80%', 'width': '45%'},  # para limitar el tamaño del contenedor
        ),
    )
