import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from clas import AVLTree  # asumiendo que tiene una implementación de AVL Tree

app = dash.Dash(__name__)


# Crear un objeto AVL Tree y agregar algunos nodos de ejemplo
tree = AVLTree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(2)
tree.insert(7)
tree.insert(15)
tree.insert(25)

# Crear un gráfico de árbol binario utilizando plotly
def create_tree_figure(tree):
    # Crear una lista de nodos y bordes
    nodes = []
    edges = []
    for node in tree.traverse_in_order():
        nodes.append(go.Scatter(x=[node.value], y=[node.depth],
                                text=[str(node.value)], mode='markers+text',
                                marker=dict(size=30), name=node.key))
        if node.parent is not None:
            edges.append(go.Scatter(x=[node.parent.value, node.value], y=[node.parent.depth, node.depth],
                                    mode='lines', name=node.parent.key))

    # Crear el layout del gráfico
    layout = go.Layout(title='Árbol binario AVL', title_x=0.5, showlegend=False,
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       hovermode='closest')

    # Devolver la figura completa del árbol
    return {'data': edges+nodes, 'layout': layout}

# Definir la aplicación de Dash
app.layout = html.Div([
    dcc.Graph(id='tree-graph', figure=create_tree_figure(tree))
])

# Crear una devolución de llamada que muestre el valor del nodo cuando se hace clic en él
@app.callback(Output('tree-graph', 'figure'), [Input('tree-graph', 'clickData')])
def display_node_value(clickData):
    if clickData is not None:
        # Obtener el valor del nodo haciendo coincidir la coordenada x del clic con un nodo en el árbol
        x_value = clickData['points'][0]['x']
        clicked_node = tree.find(x_value)

        # Actualizar la figura del árbol con el valor del nodo resaltado
        fig = create_tree_figure(tree)
        fig['data'][clicked_node.index]['marker']['color'] = 'red'

        return fig

    # Si no se ha hecho clic en ningún nodo, devolver la figura del árbol sin cambios
    return create_tree_figure(tree)

if __name__ == '__main__':
    app.run_server(debug=True)