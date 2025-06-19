from urllib.parse import urlparse, urlencode, quote, unquote, parse_qs

class UrlUtils:
    def is_valid_url(self, url):
        result = urlparse(url)
        return all([result.scheme, result.netloc])

    def encode(self, text):
        return quote(text)

    def decode(self, text):
        return unquote(text)

    def extract_query_params(self, url):
        return parse_qs(urlparse(url).query)