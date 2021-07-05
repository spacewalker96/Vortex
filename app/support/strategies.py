TELECONTACT_SCHEMA = {
    "name": None,
    "address": None,
    "description": None,
    "prestation": None,
    "phone_number": None,
    "website": None
}
TELECONTACT_STRATEGY = {
    "name": ["find_child", ["h2", {"itemprop": "name"}], ["span", {"id": "resultats_h3_span"}]],
    "address": ["find", ["div", {"class": "results-adress"}]],
    "description": ["find", ["div", {"class": "description"}]],
    "prestation": ["find_all", ["a", {"class": "rubrique-client"}]],
    "phone_number": ["find", ["div", {"class": "tel"}]],
    "website": ["get_href", ["div", {"itemprop": "url"}]]
}
