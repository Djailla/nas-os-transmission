#!/usr/bin/python

import json
import sys

TRANSMISSION_SETTINGS = '/var/lib/transmission-daemon/info/settings.json'

if len(sys.argv) < 3:
    sys.exit(1)

with open(TRANSMISSION_SETTINGS, 'r') as settings_file:
    settings = json.load(settings_file)

if sys.argv[1] not in settings:
    sys.exit(1)

value_type = type(settings[sys.argv[1]])
settings[sys.argv[1]] = value_type(sys.argv[2])

with open(TRANSMISSION_SETTINGS, 'w') as settings_file:
    json.dump(settings, settings_file, indent=4)
