import pandas

from pandas.io.excel import ExcelWriter 

csv_file = pandas.read_csv("hoteles.csv")

with ExcelWriter('hoteles.xlsx') as ew:
    csv_file.to_excel(ew) 

csv_file.to_json('hoteles.json')