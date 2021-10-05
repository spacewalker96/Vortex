import urllib.parse
import requests
from app.modules.mapper import Mapper


class Vortex(Mapper):
    def __init__(self, strategy):
        super().__init__(strategy)
        self.stats = {
            "num_results": 0,
            "num_extraction": 0
        }

    def build_request(self, request, page):
        if self.strategy.QUERY_PARAMS:
            request += urllib.parse.urlencode(self.strategy.QUERY_PARAMS)
            request += f"&page={page}"
        else:
            request += str(page)
        print(f"[+] request:{request}")
        return request

    def make_request(self, request):
        rsp = ""
        try:
            rsp = requests.get(request, headers=self.strategy.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

        except Exception as e:
            print("Error while get page results", e)

        return rsp

    def sharp_links(self, current=1, finish=None):
        print(f"[+] Start scraping using \"{self.strategy.NAME}\" strategy...")
        while True:
            request = self.build_request(self.strategy.URL, current)
            rsp = self.make_request(request)
            articles = self.get_articles(rsp)
            if articles or current == finish:
                print("[+] Done!")
                break

            self.get_links(articles)
            current += 1

        self.stats["num_results"] = len(self.links)

    def sharp_articles(self):
        print(f"[+] Getting articles...")
        for link in self.links:
            request = self.strategy.DEFAULT + link
            rsp = self.make_request(request)
            article = self.get_article(rsp)
            self.articles.append(article)
            self.stats["num_extraction"] += 1
            print(f"[+] Getting articles [{len(self.articles)}/{len(self.links)}]")
