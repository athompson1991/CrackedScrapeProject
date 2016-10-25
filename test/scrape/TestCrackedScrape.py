import unittest
from CrackedScrapeProject.src.scrape import CrackedScrape

class TestCrackedScrape(unittest.TestCase):

  def test_download(self):
    self.assertEqual(1, 1)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCrackedScrape)
unittest.TextTestRunner(verbosity=2).run(suite)
