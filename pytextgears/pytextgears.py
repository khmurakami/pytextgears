#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class TextGear():


    def __init__(self, client_key):

        if client_key is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://api.textgears.com/check.php"
        self.client_key = client_key


    def grammar_check(self, text):

        url = self.root_url

        data = {
                 'text' : '{}'.format(text),
                 'client_id': '{}'.format(self.client_key)
                }

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json
