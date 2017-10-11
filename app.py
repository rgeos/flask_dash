#!/usr/bin/env python

import dash
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server)
app.config.supress_callback_exceptions = True
