from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

tree_elements = [
    {"data": {"id": "A", "label": "A"}},
    {"data": {"id": "B", "label": "B"}},
    {"data": {"id": "C", "label": "C"}},
    {"data": {"id": "D", "label": "D"}},
    {"data": {"id": "E", "label": "E"}},
    {"data": {"id": "F", "label": "F"}},
    {"data": {"id": "G", "label": "G"}}
]
edges = [
    {'data': {'source': 'A', 'target': 'B'}},
    {'data': {'source': 'A', 'target': 'C'}},
    {'data': {'source': 'B', 'target': 'E'}},
    {'data': {'source': 'B', 'target': 'D'}},
    {'data': {'source': 'C', 'target': 'F'}},
    {'data': {'source': 'C', 'target': 'G'}},
]
stylesheet = [
    {
        "selector": 'node', # すべてのnodeに対して
        'style': {
            "opacity": 0.9,
            "label": "data(label)", # 表示させるnodeのラベル
            "background-color": "#07ABA0", # nodeの色
            "color": "#008B80" # nodeのラベルの色
        }
    },
    {
        "selector": 'edge', # すべてのedgeに対して
        "style": {
            "target-arrow-color": "#C5D3E2", # 矢印の色
            "target-arrow-shape": "triangle", # 矢印の形
            "line-color": "#C5D3E2", # edgeのcolor
            'arrow-scale': 2, # 矢印のサイズ
            'curve-style': 'bezier' # デフォルトのcurve-styleだと矢印が表示されないため指定する
    }
}]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-tree',
        elements= edges + tree_elements,
        layout={'name': 'cose'},
        style={
                'height': '95vh',
                'width': '100%'
            },
        stylesheet=stylesheet
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)