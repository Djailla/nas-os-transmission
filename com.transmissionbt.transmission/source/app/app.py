#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import redirect
from settings import bp
import json

RAINBOW_CONFIG_FILE = '/opt/transmission/.config'
RAINBOW_FLASK_PORT = 9091

try:
    with open(RAINBOW_CONFIG_FILE) as f:
        rainbow_config = json.load(f)
        RAINBOW_FLASK_PORT = rainbow_config.get('flask_port')
except:
    pass

app = Flask(__name__)
app.debug = True
app.register_blueprint(bp, url_prefix='/apps/transmission')


@app.route('/')
def home():
    return redirect("apps/transmission")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=RAINBOW_FLASK_PORT
    )
