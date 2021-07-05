import urllib.parse
import requests
from app.modules.mapper import Mapper


class Vortex(Mapper):
    def __init__(self, configs):
        super().__init__()
        self.config = configs
        self.soup = []
        self.stats = {
            "num_results": 0
        }

    def build_request(self, page):
        request = self.config.URL
        request += urllib.parse.urlencode(self.config.QUERY_PARAMS)
        request += f"&page={page}"
        print(f"[+] request:{request}")
        return request

    def get_page_results(self, request):
        partial_articles = []
        try:
            rsp = requests.get(request, headers=self.config.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

            partial_articles = self.get_articles(rsp)

        except Exception as e:
            print("Error while get page results", e)

        return partial_articles

    def get_results(self):
        page = 1
        while True:
            request = self.build_request(page)
            articles = self.get_page_results(request)
            if articles:
                self.articles.extend(articles)
            else:
                print("[+] Done!")
                break
            page += 1

        self.stats["num_results"] = len(self.soup)
