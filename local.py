import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', type='text', placeholder='Enter text'),
    html.Button('Submit', id='submit'),
    dcc.Store(id='data-store'),
    html.Div(id='output')
])

@app.callback(Output('data-store', 'data'),
              [Input('submit', 'n_clicks')],
              [State('input', 'value')])
def update_data_store(n_clicks, value):
    if n_clicks:
        return {'input': value}

@app.callback(Output('output', 'children'),
              [Input('data-store', 'data')])
def update_output(data):
    if data:
        return html.Div(data['input'])

if __name__ == '__main__':
    app.run_server(debug=True)
