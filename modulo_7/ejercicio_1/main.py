from bs4 import BeautifulSoup, Comment
import requests

soup = BeautifulSoup('<b><!--Yo soy un comentario HTML--></b>', 'html.parser')
print(soup.b.string)
print(type(soup.b.string))

comment = Comment(' #mycomment ')
soup.b.string.replace_with(comment)
print(soup.b)
print(type(soup.b.string))
