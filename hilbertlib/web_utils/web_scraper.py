from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self, headers=None):
        self.headers = headers or {'User-Agent': 'Mozilla/5.0'}

    def fetch_html(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def parse_html(self, html, tag=None, attrs=None):
        soup = BeautifulSoup(html, 'html.parser')
        if tag:
            return soup.find_all(tag, attrs=attrs)
        return soup