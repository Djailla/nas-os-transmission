#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect, url_for

import os
import json
import platform

bp = Blueprint('settings', __name__, template_folder='templates')

if platform.system() == 'Darwin':
    SHARES_ROOT_PATH = "/Users/gid509037/Perso/shares"
    TRANSMISSION_CONFIG_FILE = 'settings.json'
else:
    SHARES_ROOT_PATH = "/shares"
    TRANSMISSION_CONFIG_FILE = '/etc/transmission-daemon/settings.json'


RAINBOW_CONFIG_FILE = '/opt/transmission/.config'
RAINBOW_FLASK_PORT = 9091

try:
    with open(RAINBOW_CONFIG_FILE) as f:
        rainbow_config = json.load(f)
        RAINBOW_FLASK_PORT = rainbow_config.get('flask_port')
except:
    pass


@bp.route('/')
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
        return redirect(url_for('settings.setup_complete'))


@bp.route('/save', methods=['POST'])
def do_save_settings():
    """Save destination folder"""

    with open(TRANSMISSION_CONFIG_FILE, "r") as transmission_settings:
        data = json.load(transmission_settings)

    data['download-dir'] = request.form['dest_path']

    with open(TRANSMISSION_CONFIG_FILE, "w") as transmission_settings:
        transmission_settings.write(json.dumps(data, indent=4, sort_keys=True))

    return redirect(url_for('settings.setup_complete'))


@bp.route('/setup_complete')
def setup_complete():
    return "Setup complete"
