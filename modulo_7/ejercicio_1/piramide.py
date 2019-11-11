"""Leer archivo piramide HTML"""

from bs4 import BeautifulSoup


def cargar_html():
    with open('piramide.html', 'r') as file:
        string = file.read()
        return string


html = cargar_html()
soup = BeautifulSoup(html, 'html.parser')

producers = soup.find_all('li', {'class': 'producerlist'})
# for producer in producers:
#     print(producer.div.string)
#     print(producer.find('div', {'class': 'number'}).string)


names = soup.find_all('div', attrs={'class': 'name'})

for name in names:
    if name.string == 'tiger':
        print(name.find_parent()['class'][0])