from dash import html, dash
from pyvis.network import Network
import json


# Crea un objeto Network de Pyvis
net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white")

# Agrega nodos y aristas usando estructuras de dot
net.add_nodes([1,2,3,4],
                         title=['I am node 1', 'node 2 here', 'and im node 3', 'and im node 4'],
                         label=['NODE 1', 'NODE 2', 'NODE 3', 'NODE 4'],
                         color=['#00ff1e', '#162347', '#dd4b39', '#dd4b39'])
net.add_edges([(1,2), (1,3), (3,4)])

net.set_options("""
var options = {
  "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 3,
    "color": {
      "border": "rgba(255,255,255,1)",
      "background": "rgba(255,255,255,0.5)",
      "highlight": {
        "border": "rgba(255,255,255,1)",
        "background": "rgba(255,255,255,0.5)"
      }
    },
    "font": {
      "size": 20,
      "color": "#ffffff"
    }
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": {
      "type": "cubicBezier",
      "forceDirection": "horizontal",
      "roundness": 0.4
    }
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "direction": "UD",
      "sortMethod": "directed",
      "nodeSpacing": 200
    }
  },
  "physics": {
    "enabled": false
  }
}
""")

# Obtener el código HTML para mostrar el grafo
html_code = net.generate_html()
html_code_str = json.dumps(html_code)


# Crea la aplicación Dash
app = dash.Dash(__name__)

# Agrega el código HTML del grafo en el layout de la aplicación Dash
app.layout = html.Div([
    html.Iframe(srcDoc=html_code, width='100%', height='500')
])

if __name__ == '__main__':
    app.run_server(debug=True)
