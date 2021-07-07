import urllib.parse
import requests
from app.modules.mapper import Mapper


class Vortex(Mapper):
    def __init__(self, configs, strategy):
        super().__init__(strategy)
        self.config = configs
        self.soup = []
        self.stats = {
            "num_results": 0
        }

    def build_request(self, page):
        request = self.strategy.URL
        request += urllib.parse.urlencode(self.strategy.QUERY_PARAMS)
        request += f"&page={page}"
        print(f"[+] request:{request}")
        return request

    def get_page_results(self, request):
        end = bool
        try:
            rsp = requests.get(request, headers=self.strategy.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

            end = self.get_articles(rsp)

        except Exception as e:
            print("Error while get page results", e)

        return end

    def get_results(self):
        print("[+] Scraping start...")
        page = 1
        while True:
            request = self.build_request(page)
            end = self.get_page_results(request)
            if end:
                print("[+] Done!")
                break

            page += 1

        self.stats["num_results"] = len(self.articles)
