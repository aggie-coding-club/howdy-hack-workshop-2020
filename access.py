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
json_string = json.loads(res.text)[1]


class PageObject(object):
    userID = 0
    objID = 0
    title = ""
    body = ""

def make_page():
    page = PageObject()
    page.userID = json_string['userId']
    page.objID = json_string['id']
    page.title = json_string['title']
    page.body = json_string['body']
    return page

myPage = make_page()

print('My object properties: \nUser ID: ', myPage.userID, '\nID: ', myPage.objID, '\nTitle: ', myPage.title, '\nBody: ', myPage.body)