import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("house_rankings_2018.csv")
df.set_index("House", inplace=True)

ranked_first_bar_chart = go.Figure(
    data=[go.Bar(
        x=df.index,
        y=df.iloc[:,0]
    )],
    layout=go.Layout(
        title='Houses Ranked 1st in 2018'
    )
)

app.layout = html.Div(children=[
    html.H1(children='Dash Bootcamp'),
    html.Div(children='''
        Learn how to build web apps using dash and plotly
    '''),
    html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(len(df))]
    ),
    dcc.Graph(
        id='ranked-first',
        figure=ranked_first_bar_chart
    ),
    dcc.Dropdown(
    id='my-dropdown',
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='NYC'
    ),
    html.Div(id='output-container'),

    dcc.Dropdown(
        id='house-dropdown',
        options=[{'label': house, 'value': house} for house in df.index],
        multi=True
    ),
    html.Div(
        id='house-rankings'
    )
])
@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)
@app.callback(
    dash.dependencies.Output('house-rankings', 'children'),
    [dash.dependencies.Input('house-dropdown', 'value')])
def house_rankings(house):
    return go.Figure(
        # data=[go.Bar(
        #     x=df.columns,
        #     y=df.iloc[house,:]
        # )]
        data=[go.Bar(
            x=df.index,
            y=df.iloc[:,0]
        )]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
