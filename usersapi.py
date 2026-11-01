import requests
def fetch_json(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return None

    if response.status_code != 200:
        return None
    return response.json()
#dict_keys(['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'])
#{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}
#10
# users = 10 list od dicts
# each user:
# name, email --- text level 1
# address --- dict
#     geo --- dict
#          lat  --- text level 3
# company --- dict
#      name --- text  level 2
#users = fetch_json('https://jsonplaceholder.typicode.com/users')
#print(users[0].keys())
#print(users[0])
#print(len(users))
#print(type(users[0]['address']['geo']['lat']))

# safe_float(text)        → in: text,  out: float OR None          (helper with try/except)
# users_by_ending(users)  → in: users list, out: dict {ending: count}   # Pattern: GROUP count
# southern_count(users)   → in: users list, out: one number             # Pattern: FILTER + COUNT
# longest_company(users)  → in: users list, out: the winning user       # Pattern: BEST SO FAR
# print_report(users)

def safe_float(text):
    try:
        return(float(text))
    except ValueError:
        return None

def southern_count(users): # FILTER + COUNT
    count = 0
    for user in users:
        lat_text = user['address']['geo']['lat']
        lat = safe_float(lat_text)
        if lat is not None and lat < 0:
            count += 1
    return count

#email= users[0]['email']
#print(email)#'Sincere@april.biz'
#print(email.split('.'))# Sincere@april , biz
#print(email.split('.')[-1])# biz

def users_by_ending(users): # GROUP count
    counts = {}
    for user in users:
        email = user['email']
        ending = email.split('.')[-1]
        if ending in counts:
            counts[ending] += 1
        else:
            counts[ending] = 1
    return counts


#totals = users_by_ending(users)
#print(totals)
#print(sum(totals.values()))     # self-check: must be 10
#count = len(users[0]['company']['name'])
#for user in users:
    #print(user['company']['name'], len(user['company']['name']))

def longest_company(users):# BEST SO FAR
    best_user = None
    best_length = 0 
    for user in users:
        length = len(user['company']['name'])
        if length > best_length:
            best_length = length
            best_user = user
    return best_user
#print(longest_company(users))
#winner = longest_company(users)
#print(winner['name'], '|', winner['company']['name'])

def print_report(users):
    print(f'Loaded: {len(users)} users')

    print('Users by email ending:')
    ending = users_by_ending(users)
    for label, count in ending.items():
        print(f'     {label}: {count}')

    print(f'Southern hemisphere: {southern_count(users)} users')

    winner = longest_company(users)
    print(f'Longest company name: {winner['name']} ({winner['company']['name']})')
users = fetch_json('https://jsonplaceholder.typicode.com/users')   
if users is None:
    print('Could not load data')
else:
    print_report(users)
#users = fetch_json('https://jsonplaceholder.typicode.com/users')
#cities = [ user['address']['city'] for user in users]
#print(cities)
#print(len(cities))
      
#users = fetch_json('https://jsonplaceholder.typicode.com/users')
#mail_ending = [user['email'].split('.')[-1] for user in users]
#print(mail_ending)
#print(len(mail_ending))