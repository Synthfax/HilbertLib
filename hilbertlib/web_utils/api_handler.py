import requests

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def call_api(self, endpoint, method='GET', headers=None, payload=None):
        url = self.base_url + endpoint
        if method.upper() == 'GET':
            return requests.get(url, headers=headers, params=payload)
        elif method.upper() == 'POST':
            return requests.post(url, headers=headers, json=payload)
        elif method.upper() == 'PUT':
            return requests.put(url, headers=headers, json=payload)
        elif method.upper() == 'DELETE':
            return requests.delete(url, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")
