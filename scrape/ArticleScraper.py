from CrackedScrapeProject.scrape.AbstractScraper import AbstractScraper
from bs4 import BeautifulSoup


class ArticleScraper(AbstractScraper):

    def __init__(self, link):
        self.link = link
        self.pageCount = None
        self.article = None
        self.articleSubheadings = None
        self.intro = None
        self.entries = {}

        AbstractScraper.__init__(self, link)

    def getArticle(self):
        self.article = self.dataDictionary["soup"].find_all("article", class_="content")
        self.article = BeautifulSoup("".join([str(art.encode("utf-8")) for art in self.article]))

    def writeArticle(self, path):
        with open(path, "w") as outfile:
            outfile.write(self.article.prettify())

    def getSubheadings(self):
        subheadingList = []
        for subHeading in self.article.find_all("h2", class_="subheading"):
            div = subHeading.contents[0]
            tempStr = ""
            for divPiece in div.contents:
                tempStr = tempStr + self.__checkDivPiece(divPiece)
            subheadingList.append(tempStr)
        self.articleSubheadings = subheadingList

    def getIntro(self):
        self.intro = self.article.find("div", {"class" : "intro"}).text
        self.intro = self.__cleanText(self.intro)

    def getEntry(self, entryNumber):
        textList = []
        divClassName = "entry-" + str(entryNumber)
        entrySoup = self.article.find("div", {"class" : divClassName})
        paragraphs = entrySoup.find_all("p")
        for p in paragraphs:
            if p.get("align") == None:
                textList.append(p.text)
        fullText = " ".join(textList)
        fullText = self.__cleanText(fullText)
        self.entries[entryNumber] = fullText

    def __cleanText(self, text):
        text = text.replace("\\n", "")
        text = text.replace("\\'", "'")
        text = text.strip()
        return text

    def __checkDivPiece(self, divPiece):
        tempStr = ""
        className = str(type(divPiece))
        if(className == "<class 'bs4.element.NavigableString'>"):
            tempStr = tempStr + str(divPiece)
        elif divPiece.get("class") == None:
            tempStr = tempStr + divPiece.text
        elif divPiece.get("class")[0] != "num-wrap":
            tempStr = tempStr + divPiece.text
        return tempStr

