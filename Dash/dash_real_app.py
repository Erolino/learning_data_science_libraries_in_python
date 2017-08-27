import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import pandas as pd

ny_daily = pd.read_pickle('ny_daily')
print(ny_daily.head())

sales_by_city = pd.read_pickle('sales_by_city')
print(sales_by_city.head())
routes = sales_by_city['Route Name'].unique()

app = dash.Dash()

h1 = 'Daily Realized Sales'
first_p = '''Dash: A web application framework for Python.'''

traces = []

for day in ny_daily['Day of Week'].unique():
    filtered_ny_daily = ny_daily[ny_daily['Day of Week']==day]
    traces.append(go.Scatter(
        x = filtered_ny_daily['Travel Date'],
        y = filtered_ny_daily['Net Amount'],
        mode = 'lines',
        name = day
        ))

#print(traces)

app.layout = html.Div(children=[
    html.H1(children=h1),

    html.Div(children=first_p),

    html.Div([
        dcc.Dropdown(
            id = 'route_selection',
            options = [{'label': route, 'value': route} for route in routes],
            multi = True
        )
    ],
    style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id = 'yaxis_catagory',
            options = [{'label': item, 'value': item} for item in ['Adults','Net Amount','Occupancy']],
            value = 'Net Amount'
        )
    ],
    style={'width': '48%', 'float': 'right' ,'display': 'inline-block'}),

    html.Div([
        dcc.Graph(
            id='stops',
            figure={
                'data': traces,
                'layout': {
                    'title' : 'NY to DC Revenue by Day of the Week'

                }
            }
        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='weekly_growth_by_day',

        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})

])


@app.callback(
    dash.dependencies.Output('weekly_growth_by_day','figure'),
    [dash.dependencies.Input('yaxis_catagory','value')])

def update_weekly_growth_by_day(y_axis_catagory_name):
    df = ny_daily

    traces = []

    for day in ny_daily['Day of Week'].unique():
        filtered_ny_daily = ny_daily[ny_daily['Day of Week']==day]
        traces.append(go.Scatter(
            x = filtered_ny_daily['Travel Date'],
            y = filtered_ny_daily[y_axis_catagory_name],
            mode = 'lines',
            name = day
            ))

    return {
        'data': traces,
        'layout': {
            'title' : 'NY to DC Revenue by Day of the Week'
        }
    }


if __name__ == '__main__':
    app.run_server(port=5000, debug=True)
