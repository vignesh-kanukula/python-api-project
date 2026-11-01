import requests

#url = 'https://jsonplaceholder.typicode.com/usersz'
#response = requests.get(url)
#print(response.status_code)

#users = response.json()
#print(type(users), len(users))
#print(users[0])

# level 1 adress{street, suite..}
#level 2 geo{lat, long}
# level 1 company{name, catch phrase}
# 2. gwenborough
#name = romaguera-crona
def fetch_json(url):
    try:
        response = requests.get(url) 
    except requests.exceptions.ConnectionError:
        return None

    if response.status_code != 200:
        return None
    return response.json()

post = fetch_json('https://jsonplaceholder.typicode.com/posts/1')
print(type(post))
print(post.keys())
print(post['title'])
# <class 'dict'>
#dict_keys(['userId', 'id', 'title', 'body'])
#sunt aut facere repellat provident occaecati excepturi optio reprehenderit
