import unittest
from http.client import HTTPResponse
from CrackedScrapeProject.scrape.AbstractScraper import AbstractScraper
from bs4 import BeautifulSoup


class TestAbstractScraperMethods(unittest.TestCase):

    def setUp(self):
      self.scraper = AbstractScraper("https://docs.python.org/2/library/unittest.html")
      self.scraper.makeDataDictionary()

    def test_dataDictionaryContents(self):
      self.assertTrue(isinstance(self.scraper.dataDictionary, dict))
      self.assertTrue(isinstance(self.scraper.dataDictionary["html"], HTTPResponse))
      self.assertTrue(isinstance(self.scraper.dataDictionary["text"], bytes))
      self.assertTrue(isinstance(self.scraper.dataDictionary["soup"], BeautifulSoup))
      self.assertSetEqual(set(self.scraper.dataDictionary.keys()), set(["text", "soup", "html"]))

      

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestAbstractScraperMethods)
  unittest.TextTestRunner(verbosity=2).run(suite)