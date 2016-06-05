#!/bin/sh -e
PIDFILE=/opt/transmission/flask_app.pid
if [ -f $PIDFILE ]; then
    start-stop-daemon --stop --pidfile $PIDFILE
    rm $PIDFILE
fi

service transmission-daemon start
