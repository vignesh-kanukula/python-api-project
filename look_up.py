from helpers import fetch_json
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
    print('Could not load the data')
else:
    print_report(users, todos)
