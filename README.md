# CrackedScrapeProject

This package can scrape both simple statistics (author, view count, date published, etc) and full article text from Cracked.com.


## Simple Statistics

To scrape simple data, first make sure that the package is available in the search path for Python, then open a Python terminal and run the following:

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

## Article Text
