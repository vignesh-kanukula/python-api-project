from helpers import fetch_json,safe_float


def southern_count(users): # FILTER + COUNT
    count = 0
    for user in users:
        lat_text = user['address']['geo']['lat']
        lat = safe_float(lat_text)
        if lat is not None and lat < 0:
            count += 1
    return count

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



def longest_company(users):# BEST SO FAR
    best_user = None
    best_length = 0 
    for user in users:
        length = len(user['company']['name'])
        if length > best_length:
            best_length = length
            best_user = user
    return best_user

def print_report(users):
    print(f'Loaded: {len(users)} users')

    print('Users by email ending:')
    counts = users_by_ending(users)
    for label, count in counts.items():
        print(f'  {label}: {count}')

    print(f'Southern hemisphere: {southern_count(users)} users')

    winner = longest_company(users)
    print(f"Longest company name: {winner['name']} ({winner['company']['name']})")

users = fetch_json('https://jsonplaceholder.typicode.com/users')   
if users is None:
    print('Could not load data')
else:
    print_report(users)



