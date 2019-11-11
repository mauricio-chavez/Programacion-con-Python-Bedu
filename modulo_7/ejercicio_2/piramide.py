"""Leer archivo piramide HTML"""

from bs4 import BeautifulSoup
from bs4.element import Tag


def cargar_html():
    with open('piramide.html', 'r') as file:
        string = file.read()
        return string


html = cargar_html()
soup = BeautifulSoup(html, 'html.parser')


body = soup.contents[0].contents[1]
div = body.contents[1]

elements = div.children

for element in elements:
    if type(element) == Tag:
        print(element['id'].capitalize())
        for element in element.contents:
            if type(element) == Tag:
                name = element.contents[1].string
                number = element.contents[3].string
                print('\t-{}: {}'.format(name, number))

