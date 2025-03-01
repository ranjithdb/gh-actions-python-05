import unittest
from scraper import Scraper

class TestScrapeTitle(unittest.TestCase):
    def setUp(self):
        """Initialize the Scraper instance before each test."""
        self.scraper = Scraper("https://example.com")

    def test_fetch_html(self):
        """Test that HTML content is fetched successfully."""
        html = self.scraper.fetch_html()
        self.assertIsInstance(html, str)

    def test_parse_html(self):
        """Test that parsed HTML contains expected elements."""
        self.scraper.html = "<html><head><title>Test</title></head></html>"
        parsed_data = self.scraper.parse_html()
        self.assertEqual(parsed_data, "Test")

if __name__ == "__main__":
    unittest.main()
