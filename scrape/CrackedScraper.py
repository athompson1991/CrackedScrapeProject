from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from CrackedScrapeProject.scrape.AbstractScraper import AbstractScraper
from CrackedScrapeProject.scrape.ListEntry import ListEntry


class CrackedScraper(AbstractScraper):

    def __init__(self, year, month):
        self.currentPage = None
        self.pageCount = None
        self.listEntries = {}

        self.month = month
        self.year = year
        self.__base_url = "http://www.cracked.com/funny-articles"

        new_url = self.__base_url + ".html?date_year=" + str(year) + "&date_month=" + str(month)
        AbstractScraper.__init__(self, new_url)

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
            print(entry.encode("utf-8"))

    def getAllPages(self):
        for i in range(self.pageCount):
            self.changePage(i)
            self.getListEntries()


        # def make_df(self):
        #    self.df = pd.DataFrame({
        #        'title': self.titles
        #       ,'views': [self.data[self.titles[t]][0] for t in range(len(self.titles))]
        #       ,'author': [self.data[self.titles[t]][1] for t in range(len(self.titles))]
        #       ,'date': [self.data[self.titles[t]][2] for t in range(len(self.titles))]
        #       ,'link': [self.data[self.titles[t]][3] for t in range(len(self.titles))]

    # })
