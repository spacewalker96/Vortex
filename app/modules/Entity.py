class Entity:
    Record: object

    def __init__(self, schema):
        self.Record = schema

    def map_entity(self, data):
        # company name
        name = data.find("h2", {"itemprop": "name"}).findChild("span", {"id": "resultats_h3_span"})
        if name and name.text.strip():
            self.Record["name"] = name.text.strip()

        # company address
        address = data.find("div", {"class": "results-adress"})
        if address and address.text.strip():
            self.Record["address"] = address.text.strip()

        # company description
        description = data.find("div", {"class": "description"})
        if description and description.text.strip():
            self.Record["description"] = description.text.strip()

        # company prestations
        prestations = data.find_all("a", {"class": "rubrique-client"})
        if prestations:
            self.Record["prestation"] = ' '.join(map(lambda a: a.text.strip(), prestations))

        # company phone_number
        phone_number = data.find("div", {"class": "tel"})
        if phone_number and phone_number.text.strip():
            self.Record["phone_number"] = phone_number.text.strip()

        # company website
        website = data.find("a", {"itemprop": "url"})
        if website:
            self.Record["website"] = website.get("href")

    def get_record(self):
        return self.Record
