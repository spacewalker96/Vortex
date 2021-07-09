NAME = "Telecontact"
URL = "https://www.telecontact.ma/trouver/index.php?"
QUERY_PARAMS = {
    "nxo": "moteur",
    "nxs": "process",
    "string": "tech",
    "ou": "casablanca",
    "aproximite": "",
    "produit": ""
}
REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 "
                  "Safari/537.36 "
}
SHARP = {
    "tag": "article",
    "element": {"itemprop": "itemListElement"}
}
STRATEGY = {
    "name": ["find_child", ["h2", {"itemprop": "name"}], ["span", {"id": "resultats_h3_span"}]],
    "address": ["find", ["div", {"class": "results-adress"}]],
    "description": ["find", ["div", {"class": "description"}]],
    "prestation": ["find_all", ["a", {"class": "rubrique-client"}]],
    "phone_number": ["find", ["div", {"class": "tel"}]],
    "website": ["get_href", ["div", {"itemprop": "url"}]]
}
