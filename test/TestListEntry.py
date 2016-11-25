import unittest
from bs4 import BeautifulSoup
from CrackedScrapeProject.scrape.ListEntry import ListEntry

class TestListEntryMethods(unittest.TestCase):

    def setUp(self):
        self.rawText = '\
          <div class=listEntry>\
            <a class=linkImage href="http://www.cracked.com/article_23342_the-depressing-origins-6-cheerful-christmas-traditions.html">\
              <img data-img="http://s3.crackedcdn.com/phpimages/article/7/1/2/488712_v1.jpg" class=thumb />\
            </a>\
            <div class=meta>\
              <h3 class=title>\
                <a href="http://www.cracked.com/article_23342_the-depressing-origins-6-cheerful-christmas-traditions.html"> 6 Cheerful Christmas Traditions With Shockingly Dark Origins  </a>  \
              </h3>\
              <div class=author>\
                By <a href="http://www.cracked.com/members/Bostonpat/">Pat Carnell</a>\
              </div>\
              <div class=timeViews>\
                <span class=views>721,839 views</span> |\
                <time class=date>December 20, 2015</time>\
              </div>\
            </div>\
            <div class=clearfix></div>\
          </div>'
        self.entry = ListEntry(BeautifulSoup(self.rawText,"lxml"))


    def test_getTitle(self):
        self.entry.getTitle()
        self.assertEquals(self.entry.title, "6 Cheerful Christmas Traditions With Shockingly Dark Origins")

    def test_getLink(self):
        self.entry.getLink()
        self.assertEquals(self.entry.link, "http://www.cracked.com/article_23342_the-depressing-origins-6-cheerful-christmas-traditions.html")

    def test_getAuthor(self):
        self.entry.getAuthor()
        self.assertEquals(self.entry.author, "Pat Carnell")

    def test_getViews(self):
        self.entry.getViews()
        self.assertEquals(self.entry.views, 721839)

    def test_getDate(self):
        self.entry.getDate()
        self.assertEquals(self.entry.date.strftime("%Y-%m-%d"), "2015-12-20")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestListEntryMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
