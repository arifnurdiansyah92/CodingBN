import requests

# We're sending a new post to a blog API
api_url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    'title': 'My Great Post',
    'body': 'This is the content of my post.',
    'userId': 1
}

# Our waiter takes our new post and SENDS it to the server
response = requests.post(api_url, json=new_post)

# The server often sends a confirmation back
result = response.json()
print(result)