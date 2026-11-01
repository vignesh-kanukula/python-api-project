# fetch_json(url)             → in: takes url, out: json data
# build_name_lookup(users)    → in: users data , out: ids and names , pattern: look up
# completed_by_user(todos)    → in: total data, out: finsihed users dict, pattern: filter + group
# top_user(totals)            → in: calls 2,3 , out: one higehst item, pattern: Best so far
# print_report(todos, users)
# WHERE is the id swapped for a name, and why there?
#for user_id, count in totals.items():
 #   print(f'  {names[user_id]}: {count}')      # ← the swap happens HERE

#Why there, at the very end:

#Do all the maths with ids, and only show names. Ids are unique, but names might not be (two people could both be called “John Smith”).
#It’s like your till at work: it tracks product codes, and only the receipt shows the product names.
#Your Thursday functions keep working unchanged, since they still use ids. That’s why you can reuse them.
#print(type(users), len(users))
#print(users[0]['id'], users[0]['name'])
#<class 'list'> 200
#{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
#<class 'list'> 10
#1 Leanne Graham
#UserId from todos matches id in users 

import requests
def fetch_json(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return None

    if response.status_code != 200:
        return None
    return response.json()

def build_name_lookup(users): #LOOKUP
    names = {}
    for user in users:
        names[user['id']] = user['name']
    return names 


def completed_by_user(todos): # FILTER + GROUP count
    finished_users = {}
    for todo in todos:
        userid = todo['userId']
        if todo['completed']:
            if userid in finished_users:
                finished_users[userid] += 1
            else:
                finished_users[userid] = 1
    return finished_users


def top_user(totals):# BEST SO FAR
    highest_user = ''
    highest_total = 0
    for userid, count in totals.items():
        if count > highest_total:
            highest_total = count
            highest_user = userid
    return highest_user

def print_report(users, todos):
    names = build_name_lookup(users)
    totals = completed_by_user(todos)
    highest = top_user(totals)

    print("Completed by user:")
    for user_id, count in totals.items():
        print(f"  {names[user_id]}: {count}")

    print(f"Top user: {names[highest]} ({totals[highest]} completed)")

todos = fetch_json('https://jsonplaceholder.typicode.com/todos')
users = fetch_json('https://jsonplaceholder.typicode.com/users')   

if users is None or  todos is None:
    print('Counldnot load the data')
else:
    print_report(users, todos)

#Recap (answer in one line each, now)
#Why does the id get swapped for a name in print_report, and not earlier?
#You called print_report(todos, users), but the function expected (users, todos). What went wrong, and why did the error show up in a different function?
#What’s the difference between return response.json and return response.json()?

1. ⚠️ Half right. Ids are unique, yes. The full answer: “Do all the maths with ids, and only translate to names at display time. Ids are unique, and the old functions keep working unchanged.”

2. ⚠️ The first part is right; the “why” isn’t. It wasn’t the if line.

Python matches arguments by position, so the users parameter received the todos list.
print_report then passed that wrong list to build_name_lookup, which tried todo['name'] and crashed.
So the crash shows up where the bad data is used, not where it was sent. That’s the same lesson as the 404: errors appear downstream of the real cause.

3. ❌ “No idea”, but you fixed this exact bug at 9:44 today, and the same thing with min last week:

response.json without brackets is the function itself, like the tool sitting on the shelf.
response.json() with brackets uses the tool and gives you the result: the data.