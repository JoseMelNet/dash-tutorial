# -*- coding: utf-8 -*-

# Run this app with `python app_09_choropleth_maps.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = px.data.gapminder().query("year==2007")

fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp",  # lifeExp is a column of gapminder
                    hover_name="country",  # Column to add to hover information
                    color_continuous_scale=px.colors.sequential.Blues)

app.layout = html.Div([
    html.H1("Hello! - It is a Choropleth Map Sample",
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),

    dcc.Graph(id='choropleth-map', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
