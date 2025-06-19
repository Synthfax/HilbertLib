import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class HttpClient:
    def __init__(self, retries=3, backoff_factor=0.3):
        self.session = requests.Session()
        retry = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=(500, 502, 504)
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def get(self, url, headers=None, params=None):
        return self.session.get(url, headers=headers, params=params)

    def post(self, url, data=None, json=None, headers=None):
        return self.session.post(url, data=data, json=json, headers=headers)