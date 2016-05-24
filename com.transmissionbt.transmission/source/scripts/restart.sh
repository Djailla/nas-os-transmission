#!/bin/sh -e
PIDFILE=/opt/transmission/flask_app.pid

start-stop-daemon --stop --pidfile $PIDFILE
rm $PIDFILE

service transmission-daemon start
