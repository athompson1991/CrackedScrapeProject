from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

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
    with open(outpath, 'w'):
      f.write(article)
