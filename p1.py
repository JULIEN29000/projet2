import requests
from bs4 import BeautifulSoup

links = []

for i in range(50):
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
        outf.write('product_page_url;universal_ product_code (upc);title;price_including_tax;price_excluding_tax;number_available;category;|n review_rating;image_url;product_description')
        for row in inf:
            url = row.strip()
            reponses = requests.get(url)
            reponses.encoding = 'utf-8'
            if reponses.ok:
                soup = BeautifulSoup(reponses.text, 'html.parser')
                titre = soup.select_one('h1')
                cathegorie = soup.select('a')[3]
                description = soup.select('p')[3]
                upc = soup.select('tr')[0].select('td')[0]
                prixht = soup.select('tr')[2].select('td')[0]
                prixttc = soup.select('tr')[3].select('td')[0]
                dispo = soup.select('tr')[5].select('td')[0]
                etoile = soup.select('p')[2]
                lien = soup.find('img')['src']
                liens = 'http://books.toscrape.com/'
                lienIMG = liens + lien
                print(etoile["class"])
                print(titre.text + '\n' + cathegorie.text + ',' + description.text + '\n' + upc.text + '\n' + prixht.text + prixttc.text + dispo.text + lienIMG)
                outf.write('\n' + str(url) + ';' + upc.text + ';' + titre.text + ';' +prixttc.text + ';' + prixht.text + ';' + dispo.text + ';' + cathegorie.text + ';' + str(etoile["class"][1]) + ';' + lienIMG + ';' + description.text.replace(';', ''))













