from bs4 import BeautifulSoup

class HtmlParser:
    def get_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(strip=True)

    def find_tag(self, html, tag, attrs=None):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find_all(tag, attrs=attrs)

    def extract_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]