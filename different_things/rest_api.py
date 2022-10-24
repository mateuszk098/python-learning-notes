'''
Connect with rest api.
'''

import requests

if __name__ == "__main__":

    response = requests.get("http://jsonplaceholder.typicode.com/posts/1")
    if response.status_code != requests.codes.ok:
        print("Something has gone wrong!")
    else:
        print(response.json())

    requests_body: dict = {
        "title": "Title",
        "body": "Content",
        "userId": 1
    }

    response = requests.post("http://jsonplaceholder.typicode.com/posts", json=requests_body)
    if response.status_code != requests.codes.created:
        print("Something has gone wrong!")
    else:
        print(response.json())
