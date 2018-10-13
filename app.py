import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Dash Bootcamp'),
    html.Div(children='''
        Learn how to build web apps using dash and plotly
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
