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
        request = self.config.URL
        request += urllib.parse.urlencode(self.config.QUERY_PARAMS)
        request += f"&page={page}"
        print(f"[+] request:{request}")
        return request

    def get_page_results(self, request):
        page_results = []
        try:
            rsp = requests.get(request, headers=self.config.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

            partial_articles = self.get_articles(rsp)
            for article in partial_articles:
                # company_details = self.get_company_details(article)
                company_details = self.map_by_strategy()
                print(f"Mapped object: {company_details}")
                page_results.append(company_details)
        except Exception as e:
            print("Error while get page results", e)

        return page_results

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

        self.stats["num_results"] = len(self.articles)
