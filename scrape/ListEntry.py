from datetime import datetime

class ListEntry:
    def __init__(self, entrySoup):
        self.entrySoup = entrySoup
        self.title = None
        self.link = None
        self.author = None
        self.views = None
        self.date = None

    def getTitle(self):
        subDiv = self.entrySoup.find("div", class_="meta")
        self.title = subDiv.find("h3", class_="title").text.strip()
        self.title = self.title.replace("\t", " ")

    def getLink(self):
        try:
            self.link = self.entrySoup.find("a", class_="linkImage").get("href")
        except:
            self.link = "NULL"

    def getAuthor(self):
        try:
            self.author = self.entrySoup.find('div', class_="author").text
            self.author = self.author.replace('\n', ' ')
            self.author = self.author.replace('By ', '')
            self.author = self.author.replace('\t', ' ')
            self.author = self.author.strip()
        except AttributeError:
            self.author = "NULL"

    def getViews(self):
        try:
            self.views = self.entrySoup.find('span', class_="views")
            self.views = int(self.views.text.replace('views', '').replace(',', '').strip())
        except AttributeError:
            self.views = 0

    def getDate(self):
        try:
            self.date = self.entrySoup.find('time', class_="date")
            self.date = self.date.text
            self.date = datetime.strptime(self.date, '%B %d, %Y')
        except AttributeError:
            self.date = datetime.datetime(1970, 0, 0, 0, 0, 0, 0)
