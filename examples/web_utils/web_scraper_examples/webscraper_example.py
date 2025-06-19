from hilbertlib.web_utils.web_scraper import WebScraper

def example_web_scraper():
    scraper = WebScraper()
    html = scraper.fetch_html("https://httpbin.org/html")
    paragraphs = scraper.parse_html(html, tag="p")
    print(f"Found {len(paragraphs)} paragraph(s).")
    for p in paragraphs:
        print("-", p.text)

example_web_scraper()
