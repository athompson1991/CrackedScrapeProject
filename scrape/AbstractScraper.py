from urllib.request import urlopen
from bs4 import BeautifulSoup

class AbstractScraper:
  
  def __init__(self, url):
    self.url = url

  def getUrl(self):
    return self.url

  def createDataDictionary(self):
    html = urlopen(self.url)
    text = html.read()
    soup = BeautifulSoup(text)
    outDictionary = {"html": html, "text": text, "soup": soup}
    self.dataDictionary = outDictionary