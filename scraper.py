import requests
from bs4 import BeautifulSoup

class Scraper:
    """A simple web scraper to fetch and parse webpage titles."""

    def __init__(self, url):
        self.url = url
        self.html = ""

    def fetch_html(self):
        """Fetch the HTML content of the page."""
        response = requests.get(self.url, timeout=10)
        if response.status_code == 200:
            self.html = response.text
            return self.html
        return None

    def parse_html(self):
        """Extract the title from the fetched HTML."""
        if not self.html:
            return None
        soup = BeautifulSoup(self.html, "html.parser")
        return soup.title.string if soup.title else "No title found"

if __name__ == "__main__":
    test_url = "https://example.com"
    scraper = Scraper(test_url)
    html = scraper.fetch_html()
    print(scraper.parse_html() if html else "Failed to fetch page")
