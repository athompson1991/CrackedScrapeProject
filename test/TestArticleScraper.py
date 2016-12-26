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
        filePath = "C:/users/Alex/desktop/articleFile.html"
        self.scraper.writeArticle(filePath)
        self.writtenData = open(filePath, "r").read()
        self.assertEqual(self.scraper.article.prettify(), self.writtenData)

    def test_getSubheadings(self):
        self.scraper.getSubheadings()
        self.assertEqual("Kubrick Made Tom Cruise Walk Through A Door 95 Times In Eyes Wide Shut", self.scraper.articleSubheadings[0])
        self.assertEqual("Charlie Chaplin Made An Actress Repeat A Scene 342 Times In City Lights", self.scraper.articleSubheadings[1])
        self.assertEqual("All The References To Point Break Were The Most Expensive Part Of Hot Fuzz", self.scraper.articleSubheadings[2])
        self.assertEqual("It Took All Day To Film RoboCop Catching A Set Of Car Keys", self.scraper.articleSubheadings[3])
        self.assertEqual("The Team Behind Home Alone Went All-Out For A Fake Period Film", self.scraper.articleSubheadings[4])
        self.assertEqual("George Lucas Rebuilt A Whole Set From Return Of The Jedi 14 Years Later For A Few Seconds Of Extra Footage", self.scraper.articleSubheadings[5])
        self.assertEqual(6, len(self.scraper.articleSubheadings))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArticleScraperMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
