from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from CrackedScrapeProject.scrape.AbstractScraper import AbstractScraper as absScrape


class CrackedScraper(absScrape):
  def __init__(self, year, month):
    self.month = month
    self.year = year
    base_url = "https://www.cracked.com/funny-articles.html"
    new_url = base_url + "?date_year=" + str(year) + "&date_month=" + str(month)
    absScrape.__init__(self, new_url)

  def countPages(self):
    soup = self.dataDictionary["soup"]
    temp_val = soup.find("li", class_="paginationLastItem").text
    self.pageCount = int(temp_val)
    


  # def get_pages(self, n = -1):
  #   self.pages = []
  #   html = urlopen('http://www.cracked.com/funny-articles.html')
  #   text = html.read()
  #   mainSoup = BeautifulSoup(text)
  #   yearlist = mainSoup.find("ul", class_="accordionContent")
  #   all_links = yearlist.find_all("a", {"class": "month"}) 
  #   if n == -1:
  #     subset_lks = all_links
  #   else:
  #     subset_lks = all_links[0:n]

  #   for ref in subset_lks:
  #     self.pages.append(ref.get("href"))

  # def __get_views(div):
  #   try:
  #     viewcount = div.find('span', class_="views")
  #     return viewcount.text.replace('views', '').replace(',','').strip()
  #   except AttributeError:
  #     return '0'

  # def __get_date(div):
  #   try:
  #     getdate = div.find('time', class_="date")
  #     return getdate
  #   except AttributeError:
  #     return 'NULL'

  # def __get_author(div):
  #   try:  
  #     author = div.find('div', class_="author")
  #     return author.text.strip()
  #   except AttributeError:
  #     return "NULL"

  # def __get_link(div):
  #   try:
  #     return div.find("a", class_="linkImage").get("href")
  #   except:
  #     return 'NULL'

  
  # def get_list_entries(self):
  #   self.entries = []
  #   for listPage in self.pages:
  #     html = urlopen(listPage)
  #     text = html.read()
  #     soup = BeautifulSoup(text)
  #     body = soup.find("div", class_="body")
  #     self.entries.append(body.find_all('div', {"class":"listEntry"}))

  # def get_titles(self):
  #   self.titles = []
  #   for e in self.entries:
  #     for d in e:
  #       temp_title = d.find('h3', class_ = "title").text.strip()
  #       temp_title = temp_title.replace('\t', ' ')
  #       self.titles.append(temp_title)

  # def get_data(self):
  #   i = 0
  #   for e in self.entries:
  #     for d in e:

  #       # Parsing

  #       temp_views = get_views(d)
  #       temp_author = get_author(d)
  #       temp_date = get_date(d)
  #       temp_link = get_link(d)

  #       # Cleaning

  #       temp_date = temp_date.text
  #       temp_date = datetime.strptime(temp_date, '%B %d, %Y')
  #       temp_views = int(temp_views)
  #       temp_author = temp_author.replace('\n', ' ')
  #       temp_author = temp_author.replace('By ', '')
  #       temp_author = temp_author.replace('\t', ' ')
  #       temp_author = temp_author.strip()
  #       temp_author = temp_author.split(",")
        


  #       self.data[self.titles[i]] = [temp_views, temp_author, temp_date, temp_link]
  #       i = i + 1

  # def make_df(self):
  #    self.df = pd.DataFrame({
  #        'title': self.titles
  #       ,'views': [self.data[self.titles[t]][0] for t in range(len(self.titles))]
  #       ,'author': [self.data[self.titles[t]][1] for t in range(len(self.titles))]
  #       ,'date': [self.data[self.titles[t]][2] for t in range(len(self.titles))]
  #       ,'link': [self.data[self.titles[t]][3] for t in range(len(self.titles))]
	# })