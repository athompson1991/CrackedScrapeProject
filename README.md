# CrackedScrapeProject

This is a Python project that is a work in progress. I have established a way to use BeautifulSoup to parse the site in a scriptish manner, but am looking to build out a more object oriented approach, as well as implement test driven development (TDD) and incorporate the principles laid out in Clean Code by Robert C. Martin. The ultimate goal is to scrape both basic data (author, view count, date published, etc) and full article text from Cracked.com, load it into a pandas DataFrame, and produce interesting plots (perhaps presented using a simple Django web application).


## Basic Usage

To scrape data from Cracked.com using this package, first make sure it is in the search path for Python, then import the package into your script and run the following:

```python
from CrackedScrapeProject.scrape.CrackedScraper import CrackedScraper

myScraper = CrackedScraper()
myScraper.changeDate(2016, 6)
myScraper.getAllPages()
myScraper.makeDataFrame()
```

This produces a `DataFrame` object as imported from the `pandas` package. An entire year's data can be scraped with even fewer lines of code:

```python
from CrackedScrapeProject.scrape.CrackedScraper import CrackedScraper

myScraper = CrackedScraper()
myScraper.getYear(2016)
myScraper.makeDataFrame()
```
