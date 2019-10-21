import requests
import json
# Sending GET request to retrieve person 3
res = requests.get('https://swapi.co/api/people/3/')

# Display the response as a string
print(res.text)

# Print the dictionary form of the JSON returned from the API
print(res.json())

# Access the name of the person returned
print(res.json()["name"])
# Response JSON string object
data = res.json()


class StarWarsPerson(object):
    name = ""
    height = ""
    birthYear = ""

post = StarWarsPerson()
post.name = data['name']
post.height = data['height']
post.birthYear = data['birth_year']


print('My star wars person is: \nName: ', post.name, '\nHeight: ', post.height, '\nBirth Year: ', post.birthYear)
