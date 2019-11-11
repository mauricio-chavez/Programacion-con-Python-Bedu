"""Libros en http://books.toscrape.com/"""

import requests
from bs4 import BeautifulSoup, Comment

print('Obteniendo libros...')
response = requests.get("http://books.toscrape.com/")

html = response.content

soap = BeautifulSoup(html, 'html.parser')

articles = soap.find_all('article', attrs={'class': 'product_pod'})

books = []

for article in articles:
    title = article.h3.string
    product_price = article.find('div', attrs={'class': 'product_price'})
    price = product_price.find('p', attrs={'class': 'price_color'}).string
    books.append((title, price))


print('-' * 40)
print(' |AUTOR' + ' ' * 23 + '|PRECIO| ')
print('-' * 40)

for book in books:
    print(' |{:28}|{:8}|'.format(book[0], book[1]))

print('-' * 40)   
