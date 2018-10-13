import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('house_rankings_2018.csv')
df.set_index('House', inplace=True)
num_of_respondents = df.sum(axis=1)[0]

ranked_first_bar_chart = go.Figure(
    data=[go.Bar(
        x=df.index,
        y=df.iloc[:,0] / num_of_respondents * 100
    )],
    layout=go.Layout(
        title='Houses Ranked 1st in 2018',
        xaxis={'title': 'House'},
        yaxis={'title': '% of Respondents'}
    )
)


app.layout = html.Div(children=[
    html.H1(children='Dash Bootcamp'),
    html.Div(children='''
        Learn how to build web apps using dash and plotly
    '''),
    html.Table(
        # Header
        [html.Tr([html.Th('House')] + [html.Th(col) for col in df.columns])] +
        # Body
        [html.Tr([html.Td(df.index[i])] +
            [html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(len(df))]
    ),
    dcc.Graph(
        id='ranked-first',
        figure=ranked_first_bar_chart
    ),
    dcc.Dropdown(
        id='house-dropdown',
        options=[{'label': house, 'value': house} for house in df.index],
        # multi=True
    ),
    html.Div(
        id='house-rankings'
    )
])

@app.callback(
    dash.dependencies.Output('house-rankings', 'children'),
    [dash.dependencies.Input('house-dropdown', 'value')])
def house_rankings(house):
    return dcc.Graph(id='house-ranking-graph', figure=go.Figure(
        data=[go.Bar(
            x=df.columns,
            y=df.loc[house,:] / num_of_respondents * 100
        )],
        layout=go.Layout(
            title='{} Rankings'.format(house),
            xaxis={'title': 'Rank'},
            yaxis={'title': '% of Respondents'}
        )
    ))
    # return "it works" + house

if __name__ == '__main__':
    app.run_server(debug=True)
