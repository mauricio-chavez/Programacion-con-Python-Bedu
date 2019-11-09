import requests

response = requests.delete("https://jsonplaceholder.typicode.com/noexiste")

# if response.status_code == 404:
print(response.status_code)
posts = response.json()
print(posts)

# else:
#     print('Ha ocurrido un error')

