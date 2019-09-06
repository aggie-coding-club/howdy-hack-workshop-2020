import requests

req = requests.get('https://jsonplaceholder.typicode.com/posts')

#print(req.content)
# print(req.json())
print(req.json()[1]["title"])
