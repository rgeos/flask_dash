#!/usr/bin/env python

# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc

layout = html.Div(children=[
	html.H1("Hello Dash"),

	html.Div(id="example-graph-display", children='Dash: A web application framework for Python.'),

	dcc.Graph(
		id='example-graph',
		figure={
			'data': [
				{'x': [1, 2, 3, 4], 'y': [4, 1, 2, 5], 'type': 'bar', 'name': 'SF'},
				{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
			],
			'layout': {
				'title': 'Dash Data Visualization'
			}
		}
	),

	html.Br(),
	dcc.Link('Go to App 1', href='/app1')
])

