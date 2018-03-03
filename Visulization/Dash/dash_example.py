import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import pandas as pd

#from plotly.offline import download_plotlyjs, plot, iplot
#import cufflinks as cf
#cf.go_offline()

df = pd.read_pickle('ny_daily')
#print(df.head())

app = dash.Dash()

h1 = 'Hello Dash'
first_p = '''Dash: A web application framework for Python.'''
second_p = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div(children=[
    html.H1(children=h1),

    html.Div(children=first_p),

    dcc.Markdown(children=second_p),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Adults'], 'y': df['Net Amount'], 'type': 'scatter', 'mode': 'markers'}
            ],
            'layout': {
                'title' : 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(port=5000, debug=True)
