import unittest
from CrackedScrapeProject.scrape.ArticleScraper import ArticleScraper
from bs4 import BeautifulSoup

firstEntry = "\
Stanley Kubrick is one of the most punishingly difficult directors to work with. \
Legend says that during the filming of The Shining, he made Shelley Duvall repeat the same scene 127 times, \
which is ridiculous. The movie's assistant editor claims it was a mere 35-45 takes -- basically a cakewalk! \
On the other hand, there was that time when Kubrick broke Tom Cruise's already wobbly brain on the set of \
Eyes Wide Shut: He made the actor walk through a door repeatedly, for a total of 95 times. It was such an \
insignificant scene that no one is 100 percent sure when, exactly, it takes place in the movie. But for \
whatever reason, Kubrick needed Cruise to repeat it nearly 100 times. That's a level of perfectionism that \
crosses the line into insanity. Or perhaps we're blaming the wrong person: Maybe Tom Cruise just opens a \
door like a total asshole."

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

    def test_getIntro(self):
        self.scraper.getIntro()
        self.assertEqual(self.scraper.intro, 'Sometimes, it\'s the smallest details that really make the movie. Then again, those same seemingly-insignificant scenes can also be such an immense pain in the balls that even the most hardened Hollywood hotshot would scream "fuck it, we\'ll do a car chase instead!" Or so you\'d think ...')

    def test_getListEntry(self):
        for article in range(1, 6):
            self.scraper.getEntry(article)
        self.assertEqual(self.scraper.entries[1], firstEntry)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArticleScraperMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
