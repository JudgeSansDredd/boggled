import os
import urllib.parse

import requests


class Dictionary:
    def __init__(self):
        api_key = os.environ.get("DICTIONARY_API_KEY")
        self.encoded_query_param_api_key = urllib.parse.urlencode({
            'key': api_key
        })
        self.uri_base = f"https://dictionaryapi.com/api/v3/references"

    def get_definition(self, word):
        encoded_word = urllib.parse.quote(word)
        uri = f"{self.uri_base}/collegiate/json/{encoded_word}?{self.encoded_query_param_api_key}"
        response = requests.get(uri)
        if response.status_code != 200:
            raise Exception("Invalid request to Dictionary API")
        else:
            if type(response.json()[0]) is dict:
                # This is a definition
                return {
                    'found': True,
                    'definitions': response.json()[0]['shortdef']
                }
            else:
                # Didn't find... these are suggestions
                return {
                    'found': False,
                    'suggestions': response.json()
                }

