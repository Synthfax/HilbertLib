from hilbertlib.web_utils.url_utils import UrlUtils

def example_url_utils():
    utils = UrlUtils()
    url = "https://example.com/page?name=Synthfax&lang=python"
    print("Is valid URL?", utils.is_valid_url(url))
    params = utils.extract_query_params(url)
    print("Query params:", params)
    encoded = utils.encode("space & symbols!")
    print("Encoded:", encoded)
    decoded = utils.decode(encoded)
    print("Decoded:", decoded)

example_url_utils()
