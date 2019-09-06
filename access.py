import requests

# Sending GET request to retrieve list of posts
res = requests.get('https://jsonplaceholder.typicode.com/posts')

# Display the response as a string
# print(res.text)

# Print the dictionary form of the JSON returned from the API
# print(res.json())

# Access the title of the 2nd post returned
print(res.json()[1]["title"])
