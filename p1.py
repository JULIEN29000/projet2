import requests
from bs4 import BeautifulSoup

links = []

for i in range(2):
    url = 'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        balise_li = soup.findAll('article')
        for article in balise_li:
            a = article.find('a')
            link = a['href']
            links.append('http://books.toscrape.com/catalogue/books_1' + link)

print(len(links))

with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')


with open('urls.txt', 'r') as inf:
    with open('livres.csv', 'w', encoding="utf-8") as outf:
        outf.write('product_page_url;universal_ product_code (upc) title;price_including_tax;price_excluding_tax number_available;product_description;category|n review_rating;image_url \n')
        for row in inf:
            url = row.strip()
            reponses = requests.get(url)
            if reponses.ok:
                soup = BeautifulSoup(reponses.text, 'html.parser')
                titre = soup.select_one('h1')
                cathegorie = soup.select('a')[3]
                description = soup.select('p')[3]
                upc = soup.select('tr')[0]
                if upc is not None:
                    upc = upc.rstrip()
                prixht = soup.select('tr')[2]
                prixttc = soup.select('tr')[3]
                dispo = soup.select('tr')[5]
                etoile = soup.select('p')[2]
                lien = soup.find('img')['src']
                liens = 'http://books.toscrape.com/'
                lienIMG = liens + lien
                print(etoile["class"])
                print(titre.text + '\n' + cathegorie.text + ',' + description.text + '\n' + upc.text + '\n' + prixht.text + prixttc.text + dispo.text + lienIMG)
                outf.write('\n' + str(url) + ';' + titre.text + ';' + cathegorie.text + ';' + description.text + ';' + upc.text + ';' + prixht.text + ';' + prixttc.text + ';' + dispo.text + ';' + lienIMG + ';' + str(etoile["class"]))













