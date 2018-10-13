import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# TODO: Import the data

app.layout = html.Div(children=[
    html.H1(children='Dash Bootcamp'),
    html.H3(children='''
        Learn how to build web apps using dash and plotly
    '''),
    # TODO: Create a table of the data
])

if __name__ == '__main__':
    app.run_server(debug=True)
