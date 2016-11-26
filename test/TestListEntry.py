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
        self.entry.getTitle()
        self.entry.getLink()
        self.entry.getAuthor()
        self.entry.getViews()
        self.entry.getDate()
        self.entry.makeDictionary()


    def test_getTitle(self):
        self.assertEquals(self.entry.title, "6 Cheerful Christmas Traditions With Shockingly Dark Origins")

    def test_getLink(self):
        self.assertEquals(self.entry.link, "http://www.cracked.com/article_23342_the-depressing-origins-6-cheerful-christmas-traditions.html")

    def test_getAuthor(self):
        self.assertEquals(self.entry.author, "Pat Carnell")

    def test_getViews(self):
        self.assertEquals(self.entry.views, 721839)

    def test_getDate(self):
        self.assertEquals(self.entry.date.strftime("%Y-%m-%d"), "2015-12-20")

    def test_makeDictionary(self):
        self.assertTrue(self.entry.mainDictionary["views"], 721839)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestListEntryMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
