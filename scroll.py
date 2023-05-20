import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input, State
from dash_extensions import DeferScript


app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Input(id="input", placeholder="ID...", type="text"),
    
    html.Div(id='content', children=[
        html.Div(f'This is div {i}', id=f'div-{i}') for i in range(1000)
    ]),
    html.Button('Scroll to element', id='scroll-button'),
    html.Div(id='div-', style={}),
    dash.html.Script(),
    DeferScript(src='https://viewer.diagrams.net/js/viewer-static.min.js')
])

app.scripts.config.serve_locally = True

app.scripts.append_script({
    'external_url': 'https://code.jquery.com/jquery-3.6.0.slim.min.js',
    'strategy': 'cdn'
})

app.scripts.append_script({
    'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.9.3/umd/popper.min.js',
    'strategy': 'cdn'
})

app.scripts.append_script({
    'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
    'strategy': 'cdn'
})

app.scripts.append_script({
    'external_url': """
        $(document).on('click', '#scroll-button', function() {
            console.log('here click')
            var id = $('#input').val();
            var el = document.getElementById('div-');
            $('html, body').animate({
                scrollTop: $(el).offset().top
            }, 2000);
        });
    """
})

if __name__ == '__main__':
    app.run_server(debug=True)
