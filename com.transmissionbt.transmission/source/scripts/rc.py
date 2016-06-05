#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import platform

if __name__ == '__main__':
    if platform.system() == 'Darwin':
        TRANSMISSION_CONFIG_FILE = 'settings.json'
    else:
        TRANSMISSION_CONFIG_FILE = '/var/lib/transmission-daemon/info/settings.json'

    try:
        with open(TRANSMISSION_CONFIG_FILE) as f:
            rainbow_config = json.load(f)
            if os.path.exists(rainbow_config["download-dir"]):
                print 0
            else:
                print 1
    except:
        print 1
