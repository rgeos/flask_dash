#!/usr/bin/env python

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from apps import app1, app2, app3

app.layout = html.Div([
	dcc.Location(id='url', refresh=False),
	html.Div(id='page-content')
])


@server.route("/")
def hello():
	return "Hello Flask"


@app.callback(
	Output('page-content', 'children'),
	[Input('url', 'pathname')]
)
def display_page(pathname):
	if pathname == '/app1':
		return app1.layout
	elif pathname == '/app2':
		return app2.layout
	elif pathname == '/app3':
		return app3.layout
	else:
		return hello()


if __name__ == '__main__':
	app.run_server(debug=True, port=8001)
