from bs4 import BeautifulSoup


class Mapper:
    def __init__(self):
        self.articles = []

    def get_articles(self, response):
        partial_soup = BeautifulSoup(response.content, features="lxml")
        return partial_soup.find_all("article", {"itemprop": "itemListElement"})

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

    def get_company_details(self, company):
        company_details = {
            "name": None,
            "description": None,
            "prestations": None,
            "address": None,
            "phone_number": None,
            "email": None,
            "website": None
        }
        # company name
        name = company.find("h2", {"itemprop": "name"}).findChild("span", {"id": "resultats_h3_span"})
        if name and name.text.strip():
            company_details["name"] = name.text.strip()

            # company address
        address = company.find("div", {"class": "results-adress"})
        if address and address.text.strip():
            company_details["address"] = address.text.strip()

            # company description
        description = company.find("div", {"class": "description"})
        if description and description.text.strip():
            company_details["description"] = description.text.strip()

            # company prestations
        prestations = company.find_all("a", {"class": "rubrique-client"})
        if prestations:
            company_details["prestations"] = ' '.join(map(lambda a: a.text.strip(), prestations))

            # company phone_number
        phone_number = company.find("div", {"class": "tel"})
        if phone_number and phone_number.text.strip():
            company_details["phone_number"] = phone_number.text.strip()

        # company website
        website = company.find("a", {"itemprop": "url"})
        if website:
            company_details["website"] = website.get("href")

        return company_details