#!/usr/bin/python3

from wifi_autologin.networks import BaseNetwork
import requests

class BayernWLAN(BaseNetwork):
    SSIDs = {'@BayernWLAN'}
    CONFSEC = None

    def login(self):
        session = requests.session()
        sid = session.get("https://hotspot.vodafone.de/api/v4/session").json()['session']
        r = session.post('https://hotspot.vodafone.de/api/v4/login?sessionID=%s&action=redirect&portal=bayern' % sid, data={
            "loginProfile": "6",
            "accessType": "termsOnly",
            "session": sid,
        })


