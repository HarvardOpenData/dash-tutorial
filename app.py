import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# TODO: Import the data

# TODO: Create a table of the data

# TODO: Create a bar chart of the 1st Rankings


app.layout = html.Div(children=[
    html.H1(children='Dash Bootcamp'),
    html.H3(children='''
        Learn how to build web apps using dash and plotly
    '''),
    # TODO: Add your table here
    # TODO: Add your bar chart here
    dcc.Dropdown(
        id='house-dropdown',
        # TODO: Add the houses from the dataframe as options
        options=[]
    ),
    html.Div(
        id='house-rankings'
    )
])

@app.callback(
    dash.dependencies.Output('house-rankings', 'children'),
    [dash.dependencies.Input('house-dropdown', 'value')])
def house_rankings(house):
    # TODO: Return a graph of house rankings for house
    return None

if __name__ == '__main__':
    app.run_server(debug=True)
