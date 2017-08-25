import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import pandas as pd

#from plotly.offline import download_plotlyjs, plot, iplot
#import cufflinks as cf
#cf.go_offline()

df = pd.read_pickle('ny_daily')
print(df.head())

app = dash.Dash()

h1 = 'Daily Realized Sales'
first_p = '''Dash: A web application framework for Python.'''

traces = []

for day in df['Day of Week'].unique():
    filtered_df = df[df['Day of Week']==day]
    traces.append(go.Scatter(
        x = filtered_df['Travel Date'],
        y = filtered_df['Net Amount'],
        mode = 'lines',
        name = day
        ))

print(traces)

app.layout = html.Div(children=[
    html.H1(children=h1),

    html.Div(children=first_p),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': traces,
            'layout': {
                'title' : 'NY to DC Revenue by Day of the Week'

            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(port=5000, debug=True)
