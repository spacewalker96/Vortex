from bs4 import BeautifulSoup


class Mapper:
    def __init__(self, strategy):
        self.strategy = strategy
        self.map = strategy.STRATEGY
        self.articles = []
        self.records = []
        self.links = []

    def get_links(self, response):
        beauty_soup = BeautifulSoup(response.content, features="lxml")
        new_links = beauty_soup.find_all(self.strategy.LINK["tag"],
                                         self.strategy.LINK["element"])
        print(f"[+] Get {len(new_links)} new links...")
        if new_links:
            for link in new_links:
                self.links.append(link.get("href"))

    def get_articles(self, response):
        beauty_soup = BeautifulSoup(response.content, features="lxml")
        new_articles = beauty_soup.find_all(self.strategy.ARTICLES["tag"],
                                            self.strategy.ARTICLES["element"])
        print(f"[+] Get {len(new_articles)} new articles...")
        if new_articles:
            for article in new_articles:
                self.articles.append(article)
            return False
        else:
            return True

    def get_article(self, response):
        beauty_soup = BeautifulSoup(response.content, features="lxml")
        new_article = beauty_soup.find(self.strategy.ARTICLE["tag"],
                                       self.strategy.ARTICLE["element"])
        return new_article

    def extract_data(self):
        index = 0
        print("[+] Extracting data...")
        for article in self.articles:
            self.map_by_strategy(index)
            index += 1

    def map_by_strategy(self, index):
        funcs = self.load_funcs()
        mapped_object = {}
        for target in self.map:
            if self.map[target][0] == "find_child":
                data_child = funcs[self.map[target][0]](index,
                                                        self.map[target][1][0], self.map[target][1][1],
                                                        self.map[target][2][0], self.map[target][2][1])
                mapped_object[target] = data_child
            else:
                data = funcs[self.map[target][0]](index, self.map[target][1][0], self.map[target][1][1])
                mapped_object[target] = data
        print(mapped_object)
        self.records.append(mapped_object)

    def load_funcs(self):
        stored_funcs = {
            "find": self.find,
            "find_child": self.find_child,
            "find_all": self.find_all,
            "get_href": self.get_href,
        }
        return stored_funcs

    def find(self, index, tag, target=None):
        data = self.articles[index].find(tag, target)
        if data and data.text.strip():
            return data.text.strip()

    def find_child(self, index, tag, target, child_tag, child_target=None):
        data = self.articles[index].find(tag, target).findChild(child_tag, child_target)
        if data and data.text.strip():
            return data.text.strip()

    def find_all(self, index, tag, target=None):
        data = self.articles[index].find_all(tag, target)
        if data:
            map_data = ' '.join(map(lambda a: a.text.strip(), data))
            return map_data

    def get_href(self, index, tag, target=None):
        data = self.articles[index].find(tag, target)
        if data:
            return data.get("href")
