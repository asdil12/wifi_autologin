#!/usr/bin/python3

from wifi_autologin.networks import BaseNetwork
import requests

class DeutscheBahnWLAN(BaseNetwork):
    SSIDs = {'WIFIonICE', 'WIFI@DB'}
    CONFSEC = None

    def login(self):
        session = requests.session()
        session.get("https://wifi.bahn.de/de/")
        r = session.post('https://wifi.bahn.de/de/', data={
            "login": "true",
            "CSRFToken": session.cookies['csrf'],
        })


