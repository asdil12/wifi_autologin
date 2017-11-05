#!/usr/bin/python3

from wifi_autologin.networks import BaseNetwork
import requests

class Telekom(BaseNetwork):
    SSIDs = {'Telekom'}
    CONFSEC = 'telekom'

    def login(self):
        requests.get("https://hotspot.t-mobile.net/wlan/index.do", params={
            "username": self.conf['username'],
            "password": self.conf['password'],
            "strHinweis": "Zahlungsbedingungen",
            "strAGB": "AGB",
        })
