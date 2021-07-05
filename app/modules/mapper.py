from bs4 import BeautifulSoup


class Mapper:
    def __init__(self):
        self.articles = []

    def get_articles(self, response):
        partial_soup = BeautifulSoup(response.content, features="lxml")
        return self.soup.find_all("article", {"itemprop": "itemListElement"})

    def map_by_strategy(self, strategy):
        frame = 0
        funcs = self.load_funcs()
        for action in strategy:
            if action == "find_child":
                funcs[action](strategy[action][0][0],
                              strategy[action][0][1],
                              strategy[action][1][0],
                              strategy[action][1][1])
            else:
                funcs[action](action[0][0], action[0][1])
            frame += 1

    def load_funcs(self):
        stored_funcs = {
            "find": self.find,
            "find_child": self.find_child,
            "find_all": self.find_all,
            "get_href": self.get_href
        }
        return stored_funcs

    def find(self, tag, target):
        data = self.articles.find(tag, target)
        if data and data.text.strip():
            return data.text.strip()

    def find_child(self, tag, target, child_tag, child_target):
        data = self.articles.find(tag, target).findChild(child_tag, child_target)
        if data and data.text.strip():
            return data.text.strip()

    def find_all(self, tag, target):
        data = self.articles.find_all(tag, target)
        if data:
            map_data = ' '.join(map(lambda a: a.text.strip(), data))
            return map_data

    def get_href(self, tag, target):
        data = self.articles.find(tag, target)
        if data:
            return data.get("href")
