from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_views(div):
      try:
        viewcount = div.find('span', class_="views")
        return viewcount.text.replace('views', '').replace(',','').strip()
      except AttributeError:
        return '0'

def get_date(div):
    try:
      getdate = div.find('time', class_="date")
      return getdate
    except AttributeError:
      return 'NULL'

def get_author(div):
    try:  
      author = div.find('div', class_="author")
      return author.text.strip()
    except AttributeError:
      return "NULL"

def get_link(div):
    try:
      return div.find("a", class_="linkImage").get("href")
    except:
      return 'NULL'

class CrackedScrape:

  def __init__(self):
    self.pages = []
    self.entries = []
    self.titles = []
    self.data = {}

  def get_pages(self, n = -1):
    self.pages = []
    html = urlopen('http://www.cracked.com/funny-articles.html')
    text = html.read()
    mainSoup = BeautifulSoup(text)
    yearlist = mainSoup.find("ul", class_="accordionContent")
    all_links = yearlist.find_all("a", {"class": "month"}) 
    if n == -1:
      subset_lks = all_links
    else:
      subset_lks = all_links[0:n]

    for ref in subset_lks:
      self.pages.append(ref.get("href"))
  
  def get_list_entries(self):
    self.entries = []
    for listPage in self.pages:
      html = urlopen(listPage)
      text = html.read()
      soup = BeautifulSoup(text)
      body = soup.find("div", class_="body")
      self.entries.append(body.find_all('div', {"class":"listEntry"}))

  def get_titles(self):
    self.titles = []
    for e in self.entries:
      for d in e:
        temp_title = d.find('h3', class_ = "title").text.strip()
        temp_title = temp_title.replace('\t', ' ')
        self.titles.append(temp_title)

  def get_data(self):
    i = 0
    for e in self.entries:
      for d in e:

        # Parsing

        temp_views = get_views(d)
        temp_author = get_author(d)
        temp_date = get_date(d)
        temp_link = get_link(d)

        # Cleaning

        temp_date = temp_date.text
        temp_date = datetime.strptime(temp_date, '%B %d, %Y')
        temp_views = int(temp_views)
        temp_author = temp_author.replace('\n', ' ')
        temp_author = temp_author.replace('By ', '')
        temp_author = temp_author.replace('\t', ' ')
        temp_author = temp_author.strip()
        temp_author = temp_author.split(",")
        


        self.data[self.titles[i]] = [temp_views, temp_author, temp_date, temp_link]
        i = i + 1

  def make_df(self):
     self.df = pd.DataFrame({
         'title': self.titles
        ,'views': [self.data[self.titles[t]][0] for t in range(len(self.titles))]
        ,'author': [self.data[self.titles[t]][1] for t in range(len(self.titles))]
        ,'date': [self.data[self.titles[t]][2] for t in range(len(self.titles))]
        ,'link': [self.data[self.titles[t]][3] for t in range(len(self.titles))]
	})
  
  def write_data(self, out_path):
     self.df.to_csv(out_path)


class ArticleScrape:

  def __init__(self, scrape_obj):
    self.scrape = scrape_obj
    self.articles = {}
    self.article_texts = {}
    self.list_entries = {}

  def get_article(self, title):
    temp_ls = []
    temp_link = self.scrape.data[title][3]
    article = BeautifulSoup(urlopen(temp_link).read())
    article = BeautifulSoup(article.encode('utf-8'))
    pagination = article.find_all('span', class_='paginationNumber')
    temp_ls.append(article)
    if len(pagination) != 0:
      max_page = pagination[1].text
      for pg in range(0, int(max_page)):
        try:
          nextUrl = article.find('a', class_ = 'next').get('href')
          article = BeautifulSoup(urlopen(nextUrl).read())
          temp_ls.append(article)
        except:
          pass
    self.articles[title] = temp_ls

  def get_lists(self, title):
    article_raw = self.articles[title]
    temp_ls = []
    for pg in article_raw:
      for sh in pg.find_all("h2", class_ = "subheading"):
        temp_ls.append(sh.text)
    self.list_entries[title] = temp_ls


  def get_text(self, title):
    article_raw = self.articles[title]
    temp_ls = []
    for pg in article_raw:
      for p in pg.find_all('p'):
        temp_ls.append(p.text)
    self.article_texts[title] = temp_ls
  
  def write_data(self, title, outpath):
    article = self.article_texts[title]
    article = ' '.join(article)
    with open(outpath, 'w') as f:
      f.write(article)