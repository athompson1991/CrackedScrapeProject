class ListEntry:
    def __init__(self, entry):
        self.entry = entry
        self.title = None
        self.link = None
        self.author = None
        self.views = None
        self.date = None

    def getTitle(self):
        subDiv = self.entry.find("div", class_="meta")
        self.title = subDiv.find("h3", class_="title").text.strip()
        self.title = self.title.replace("\t", " ")
