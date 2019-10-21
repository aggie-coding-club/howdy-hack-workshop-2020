import requests
import json
# Sending GET request to retrieve list of posts
res = requests.get('https://jsonplaceholder.typicode.com/posts')

# Display the response as a string
# print(res.text)

# Print the dictionary form of the JSON returned from the API
# print(res.json())

# Access the title of the 2nd post returned
print(res.json()[1]["title"])
# Response JSON string object
data = res.json()[1]


class PostObject(object):
    userID = 0
    objID = 0
    title = ""
    body = ""

post = PostObject()
post.userID = data['userId']
post.objID = data['id']
post.title = data['title']
post.body = data['body']


print('My object properties: \nUser ID: ', post.userID, '\nID: ', post.objID, '\nTitle: ', post.title, '\nBody: ', post.body)
