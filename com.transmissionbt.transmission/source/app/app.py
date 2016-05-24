#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for

import os
import json

app = Flask(__name__)
app.debug = True
app.config["APPLICATION_ROOT"] = "/apps/transmission/"

SHARES_ROOT_PATH = "/shares"
# SHARES_ROOT_PATH = "/Users/gid509037/Perso/shares"

TRANSMISSION_CONFIG_FILE = '/etc/transmission-daemon/settings.json'

RAINBOW_CONFIG_FILE = '/opt/transmission/.config'
RAINBOW_FLASK_PORT = 9091
RAINBOW_BT_PORT = 9092

try:
    with open(RAINBOW_CONFIG_FILE) as f:
        rainbow_config = json.load(f)
        RAINBOW_FLASK_PORT = rainbow_config.get('flask_port')
        RAINBOW_BT_PORT = rainbow_config.get('tm_port')
except:
    pass


@app.route('/')
def home():
    json_data = open(TRANSMISSION_CONFIG_FILE)
    data = json.load(json_data)
    json_data.close()

    dl_dir = data['download-dir']

    if not dl_dir or not os.path.exists(data['download-dir']):
        try:
            path_list = ''.join(
                '<option>%s</option>\n' % os.path.join(SHARES_ROOT_PATH, folder)
                for folder in os.listdir(SHARES_ROOT_PATH)
                if not folder.startswith('.')
            )
        except:
            path_list = '<option>No folder available</option>'

        return render_template('settings.tpl', path_list=path_list)
    else:
        return redirect(url_for('setup_complete'))


@app.route('/save', methods=['POST'])
def do_save_settings():
    """Save destination folder"""

    with open(TRANSMISSION_CONFIG_FILE, "r") as transmission_settings:
        data = json.load(transmission_settings)

    data['download-dir'] = request.form['dest_path']

    with open(TRANSMISSION_CONFIG_FILE, "w") as transmission_settings:
        transmission_settings.write(json.dumps(data, indent=4, sort_keys=True))

    return redirect(url_for('setup_complete'))


@app.route('/setup_complete')
def setup_complete():
    return "Setup complete"

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=RAINBOW_FLASK_PORT
    )
