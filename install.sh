#!/bin/sh

if [ ! -f /usr/bin/iwgetid ] ; then
	echo "Error: Install iwgetid (pkg: wireless_tools) first"
	exit 1
fi

cp -v 02hotspot /etc/NetworkManager/dispatcher.d/
if [ ! -f /etc/wifi_autologin.conf ] ; then
	cp -v wifi_autologin.conf /etc/
fi

python3 setup.py install
