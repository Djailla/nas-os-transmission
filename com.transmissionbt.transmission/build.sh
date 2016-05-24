#!/bin/bash

/bin/echo -e '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d
chmod +x /usr/sbin/policy-rc.d

apt-get update
apt-get install -y -q --no-install-recommends transmission-daemon python-pip

pip install flask

rm /usr/sbin/policy-rc.d

mkdir -p /var/run/transmission-daemon
chown debian-transmission:debian-transmission /var/run/transmission-daemon

install -m 755 /home/source/rc.local /etc
install -m 755 /home/source/settings.json /etc/transmission-daemon
install -m 755 /home/source/etc/default/transmission-daemon /etc/default
install -m 755 /home/source/etc/init.d/transmission-daemon /etc/init.d/

mkdir -m 755 -p /opt/transmission
cp -r /home/source/app/* /opt/transmission

exit 0
