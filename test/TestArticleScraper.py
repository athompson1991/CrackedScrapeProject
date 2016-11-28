import unittest
from CrackedScrapeProject.scrape.ArticleScraper import ArticleScraper
from bs4 import BeautifulSoup

class TestArticleScraperMethods(unittest.TestCase):

    def setUp(self):
        articleChoice = "http://www.cracked.com/article_24424_6-extremely-minor-movie-scenes-that-cost-fortune-to-film.html"
        self.scraper = ArticleScraper(articleChoice)
        self.scraper.makeDataDictionary()
        self.scraper.getArticle()

    def test_getArticle(self):
        self.assertTrue(isinstance(self.scraper.article, BeautifulSoup))

    def test_writeArticle(self):
        filePath = "C:/users/athompson/desktop/articleFile.html"
        self.scraper.writeArticle(filePath)
        self.writtenData = open(filePath, "r").read()
        self.assertEqual(self.scraper.article.prettify(), self.writtenData)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArticleScraperMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
