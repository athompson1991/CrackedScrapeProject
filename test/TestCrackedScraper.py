import unittest
from CrackedScrapeProject.scrape.CrackedScraper import CrackedScraper
from bs4 import BeautifulSoup


class TestCrackedScraperMethods(unittest.TestCase):

    def setUp(self):
      self.scraper = CrackedScraper(2016, 10)
      self.scraper.makeDataDictionary()
      self.scraper.countPages()

    def test_getPageCount(self):
      self.assertEquals(self.scraper.pageCount, 11)
      self.assertTrue(isinstance(self.scraper.pageCount, int))


      

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCrackedScraperMethods)
  unittest.TextTestRunner(verbosity=2).run(suite)

