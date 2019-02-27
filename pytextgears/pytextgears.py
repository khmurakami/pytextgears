#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears.error_handling import *

import requests
import json

class TextGear():

    def __init__(self, client_key):

        if client_key is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://api.textgears.com/check.php"
        self.client_key = client_key

    def grammar_checker(self, text):

        """Get pagnation Resources

        Args:
            text (string): Text you want to have TextGear grammar checked

        Return:
            raw_json (dict): Dictionary of the result json requested

        Raises:
            Exception error: Uses HTTP error handler to check status code
        """

        url = self.root_url

        data = {
                 'text' : '{}'.format(text),
                 'client_id': '{}'.format(self.client_key)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json
