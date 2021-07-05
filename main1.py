import re

import requests
from bs4 import BeautifulSoup
from lxml import etree
import psycopg2

conn = psycopg2.connect(
        database="python_test", user='postgres', password='admin', host='127.0.0.1', port='5432'
    )
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()



sos_title = []
sos_links = []
# sos_adresse = []
# sos_phone = []
# sos_email =[]
# sos_website = []
# sos_activity = []
# sos_capital = []
# sos_fax = []



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
page_number = 1
while True:

    result = requests.get(f"https://charika.ma/societes-{page_number}", headers=header)
    src = result.content
    soup = BeautifulSoup(src,"lxml")

    page_limit = 2
    if(page_number > page_limit):
        print("page end")
        break


    link_tag = soup.findAll('h5', attrs={'class': 'strong text-lowercase truncate'})

    for i in range(len(link_tag)):
        sos_links.append("https://charika.ma/"+link_tag[i].find("a").attrs['href'])
    page_number += 1
    print("page switched")

for link in sos_links:
    webpage = requests.get(link, headers=header)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    adress =  dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[3]/div[1]/span[2]/label/text()')
    capital = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[4]/div/div[1]/table/tbody/tr[3]/td[2]/text()')
    title = str(dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[1]/h1/a/text()'))
    phone = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/span/span[2]/text()')
    fax = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[2]/span/span[2]/text()')
    e_email = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[3]/span/a/text()')
    website = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[4]/span/a/text()')
    activity = dom.xpath('//*[@id="fiche"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/span/h2/text()')


    title = title.split()
    print(" ".join(title))

    # print(re.sub(r"[\r\n\t]*", "", title))

    # postgres_insert_query = """ INSERT INTO societe_table(title, adress, phone, fax,email,website,activity,capital) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    # record_to_insert = (title,adress, phone,fax,e_email, website,activity,capital)
    # cursor.execute(postgres_insert_query, record_to_insert)


    # sos_adresse.append(adress)
    # sos_capital.append(capital)
    # sos_title.append(title)
    # sos_phone.append(phone)
    # sos_fax.append(fax)
    # sos_email.append(e_email)
    # sos_website.append(website)
    # sos_activity.append(activity)

# print(sos_activity ,sos_capital)
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()
