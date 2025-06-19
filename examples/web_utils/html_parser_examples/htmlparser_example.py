from hilbertlib.web_utils.html_parser import HtmlParser

def example_html_parser():
    html = """
    <html><body>
    <h1>Welcome</h1>
    <a href="https://google.com">Google</a>
    <a href="https://openai.com">OpenAI</a>
    </body></html>
    """
    parser = HtmlParser()
    text = parser.get_text(html)
    links = parser.extract_links(html)
    print("Page text:", text)
    print("Links found:", links)

example_html_parser()
