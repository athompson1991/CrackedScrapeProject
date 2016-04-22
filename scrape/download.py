import CrackedScrape as mod

cs = mod.CrackedScrape()
cs.get_pages()
cs.get_list_entries()
cs.get_titles()
cs.get_data()

articles = mod.ArticleScrape(cs)
i = 1
for t in cs.titles:
  articles.get_article(t)
  articles.get_lists(t)
  articles.get_text(t)
  articles.write_data(t, "articles/" + str(i) + ".txt")
  i = i + 1
