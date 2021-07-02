from bs4 import BeautifulSoup
import urllib.parse
import requests


class Vortex:
    def __init__(self, base_url, params, page):
        self.BaseUrl = base_url
        self.Params = params
        self.Page = page
        self.Request = self.BaseUrl

    def build_request(self):
        self.Request += urllib.parse.urlencode(self.Params)
        self.Request += f"&page={self.Page}"

    def get_page_results(self, url, headers):
        page_results = []

        try:
            rsp = requests.get(url, headers=headers)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

            soup = BeautifulSoup(rsp.content, features="lxml")

            companies = soup.find_all("article", {"itemprop": "itemListElement"})
            for company in companies:
                company_details = get_company_details(company)
                page_results.append(company_details)
        except Exception as e:
            print("Error while get page results", e)

        return page_results

    def get_results(self, configs):
        results = []
        stats = {
            "num_results": 0
        }

