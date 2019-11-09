from bottle import route, run, template

from products import get_products
from template_generator import bedu_travels_template

@route("/")
def index():
    products = get_products()
    html = bedu_travels_template(products)
    return template(html)


run(host="localhost", port=8080, reloader=True)
