#!/usr/bin/python3

from distutils.core import setup

setup(                                                                                                                                         
	name='wifi_autologin',
	version='0.0.1',
	license='GPL',
	description='Wireless Autologin to Hotspots',
	author='Dominik Heidler',
	author_email='dominik@heidler.eu',
	url='http://github.com/asdil12/wifi_autologin',
	#requires=['flask', 'flup'],
	packages=['wifi_autologin', 'wifi_autologin.networks'],
	scripts=['bin/wifi_autologin'],
)

