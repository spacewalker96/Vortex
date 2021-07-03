import urllib.parse
import requests
from bs4 import BeautifulSoup


class Vortex:
    def __init__(self, configs):
        self.Config = configs

    def build_request(self, page):
        request = self.Config.URL
        request += urllib.parse.urlencode(self.Config.QUERY_PARAMS)
        request += f"&page={page}"
        print(f"[+] request:{request}")
        return request

    def get_page_results(self, request, entity):
        page_results = []

        try:
            rsp = requests.get(request, headers=self.Config.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

            soup = BeautifulSoup(rsp.content, features="lxml")

            articles = soup.find_all("article", {"itemprop": "itemListElement"})
            for article in articles:
                entity.map_entity(article)
                company_details = entity.get_record()
                page_results.append(company_details)
        except Exception as e:
            print("Error while get page results", e)

        return page_results

    def get_results(self, entity):
        results = []
        stats = {
            "num_results": 0
        }

        page = 1
        while True:
            request = self.build_request(page)
            page_results = self.get_page_results(request, entity)
            if page_results:
                results.extend(page_results)
            else:
                print("[+] Done!")
                break
            page += 1

        stats["num_results"] = len(results)

        return results, stats
