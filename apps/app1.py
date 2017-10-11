#!/usr/bin/env python

# -*- coding: utf-8 -*-

from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div([
	html.H3("App 1"),

	dcc.Dropdown(
		id="app-1-dropdown",
		options=[
			{'label': f'App 1 - {i}', 'value': i} for i in ['NYC', 'MTL', 'LA']
		]
	),


	html.Br(),
	html.Div(id='app-1-display-value'),

	html.Br(),
	dcc.Link('Go to App 2', href='/app2')

])


@app.callback(
	Output('app-1-display-value', 'children'),
	[Input('app-1-dropdown', 'value')]
)
def display_value(value):
	return f'You have selected {value}'
