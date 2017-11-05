#!/usr/bin/python3

import os
from importlib import import_module
import inspect

class BaseNetwork(object):
    SSIDs = set()
    CONFSEC = None

    def __init__(self, ssid, bssid, conf=None):
        self.ssid = ssid
        self.bssid = bssid
        self.conf = conf

    def login(self):
        pass

class AutologinManager(object):
    def __init__(self, conf):
        self.conf = conf
        self.ssid_table = {}
        for module in os.listdir(os.path.dirname(__file__)):
            if module == '__init__.py' or module[-3:] != '.py' or module == '__pycache__':
                continue
            m = import_module('wifi_autologin.networks.%s' % module[:-3])
            for name, obj in inspect.getmembers(m):
                if inspect.isclass(obj) and issubclass(obj, BaseNetwork) and obj is not BaseNetwork:
                    for ssid in obj.SSIDs:
                        self.ssid_table[ssid] = obj

    def login(self, ssid, bssid):
        assert ssid in self.ssid_table, "No implementation found for ssid '%s'" % ssid
        Network = self.ssid_table[ssid]
        netconf = self.conf[Network.CONFSEC] if Network.CONFSEC else None
        net = Network(ssid, bssid, netconf)
        return net.login()
