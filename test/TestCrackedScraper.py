import unittest
from CrackedScrapeProject.scrape.CrackedScraper import CrackedScraper


class TestCrackedScraperMethods(unittest.TestCase):

  def setUp(self):
    self.scraper = CrackedScraper(2016, 10)
    self.scraper.makeDataDictionary()
    self.scraper.countPages()

  def test_getPageCount(self):
    self.assertEquals(self.scraper.pageCount, 11)
    self.assertTrue(isinstance(self.scraper.pageCount, int))

  def test_changePageGoodURL(self):
    self.scraper.changePage(3)
    new_url = self.scraper.url
    self.assertEqual(new_url, "http://www.cracked.com/funny-articles_p3.html?date_year=2016&date_month=10")

  def test_changePageGoodContents(self):
    old_text = self.scraper.dataDictionary["text"]
    self.scraper.changePage(8)
    new_text = self.scraper.dataDictionary["text"]
    self.assertNotEqual(old_text, new_text)

  def test_getListEntries(self):
    self.scraper.getListEntries()
    self.assertEqual(len(self.scraper.listEntries), 15)
    self.assertTrue(isinstance(self.scraper.listEntries, dict))

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCrackedScraperMethods)
  unittest.TextTestRunner(verbosity=2).run(suite)

