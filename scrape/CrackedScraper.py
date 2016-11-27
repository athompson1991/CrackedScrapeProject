import pandas as pd
from CrackedScrapeProject.scrape.AbstractScraper import AbstractScraper
from CrackedScrapeProject.scrape.ListEntry import ListEntry


class CrackedScraper(AbstractScraper):

    def __init__(self):
        self.month = None
        self.year = None
        self.pageCount = None
        self.currentPage = None
        self.listEntries = {}
        self.listEntryDataFrame = None

        self.__base_url = "http://www.cracked.com/funny-articles"

        AbstractScraper.__init__(self, self.__base_url + ".html")

    def changeDate(self, yearNumber, monthNumber):
        self.url = self.__base_url + "_p1.html?date_year=" + str(yearNumber) + "&date_month=" + str(monthNumber)
        self.currentPage = 1
        self.month = monthNumber
        self.year = yearNumber
        self.makeDataDictionary()

    def countPages(self):
        soup = self.dataDictionary["soup"]
        temp_val = soup.find("li", class_="paginationLastItem").text
        self.pageCount = int(temp_val)

    def changePage(self, pageNumber):
        self.currentPage = pageNumber
        self.url = self.__base_url + "_p" + str(pageNumber) + ".html?date_year=" + str(self.year) + "&date_month=" + str(self.month)
        self.makeDataDictionary()

    def getListEntries(self):
        body = self.dataDictionary["soup"].find("div", class_="body")
        entriesSoup = body.find_all('div', {"class": "listEntry"})
        for soup in entriesSoup:
            entry = ListEntry(soup)
            entry.getTitle()
            entry.getLink()
            entry.getAuthor()
            entry.getViews()
            entry.getDate()
            entry.makeDictionary()
            self.listEntries[entry.title] = entry.mainDictionary

    def printTitles(self):
        for entry in self.listEntries:
            print(str(entry.encode("utf-8")))

    def getAllPages(self):
        for i in range(self.pageCount):
            self.changePage(i)
            self.getListEntries()

    def getYear(self, yearNumber):
        for m in range(1, 12):
            self.changeDate(yearNumber, m)
            self.countPages()
            self.getAllPages()

    def makeDataFrame(self):
        self.listEntryDataFrame = pd.DataFrame.from_dict(self.listEntries).transpose()



