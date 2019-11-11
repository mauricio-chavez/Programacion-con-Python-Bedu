"""Beautiful Soup BEDU"""

import requests
from bs4 import BeautifulSoup, Comment

# Tag
response = requests.get("http://www.google.com")

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.string)
print(soup.find_all("img"))


# Navigable String
soup = BeautifulSoup(
    '<p class="bold hola hola-2" id="1" height="40" >Saludos!</p>', 'html.parser'
)
tag = soup.p
tag.name = 'h1'

tag.string.replace_with('Hola!')
print(tag)

# Comment
soup = BeautifulSoup(
    "<h1><!--Yo soy un comentario HTML--></h1>", 'html.parser')
tag = soup.h1
tag.string.replace_with(Comment('Soy un comentario'))
print(tag)
