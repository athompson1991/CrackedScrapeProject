from urllib.request import urlopen
from bs4 import BeautifulSoup

class AbstractScraper:
  
  def __init__(self, url):
    self.url = url
    self.dataDictionary =  None


  def makeDataDictionary(self):
    html = urlopen(self.url)
    text = html.read()
    soup = BeautifulSoup(text, "lxml")
    self.dataDictionary = {"html": html, "text": text, "soup": soup}

