import requests
import json

# Sending GET request to retrieve post 1
res = requests.get('https://jsonplaceholder.typicode.com/posts/1/')

# Display the response as a string
print(res.text)

# Print the dictionary form of the JSON returned from the API
print("\n\n", res.json())

# Access the title of the post returned
print("\n\ntitle:", res.json()["title"])

# Response JSON string object
data = res.json()


class Post(object):
    userId = ""
    id = ""
    title = ""
    body = ""

    def to_dict(self):
        return {
            'userId' : self.userId,
            'id' : self.id,
            'title' : self.title,
            'body' : self.body
        }

post = Post()
post.userId = 1
post.id = 2021
post.title = "Howdy Hack"
post.body = "Ayy Whoop"

print('\n\nMy post is: ', post.to_dict())

res = requests.post('https://jsonplaceholder.typicode.com/posts/', post.to_dict())

print(res.text)
