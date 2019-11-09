import csv

def get_products():
    products = []
    with open('travels.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)

    return products