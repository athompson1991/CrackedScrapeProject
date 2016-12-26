import unittest
from CrackedScrapeProject.test.TestArticleScraper import TestArticleScraperMethods
from CrackedScrapeProject.test.TestAbstractScraper import TestAbstractScraperMethods
from CrackedScrapeProject.test.TestCrackedScraper import TestCrackedScraperMethods
from CrackedScrapeProject.test.TestListEntry import TestListEntryMethods

class_list = [TestAbstractScraperMethods, TestArticleScraperMethods, TestCrackedScraperMethods, TestArticleScraperMethods]
for tempClass in class_list:
    suite = unittest.TestLoader().loadTestsFromTestCase(tempClass)
    unittest.TextTestRunner(verbosity=2).run(suite)

