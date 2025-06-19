import requests

class Webhook:
    def __init__(self, url):
        self.url = url

    def send(self, data, headers=None):
        response = requests.post(self.url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
