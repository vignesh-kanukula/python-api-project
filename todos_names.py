
from helpers import fetch_json


def completed_count(todos): # FILTER + COUNT
    finished = [todo for todo in todos if todo['completed']]
    return len(finished)

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

def titles_for_user(todos, user_id): # FILTER + TRANSFORM
    titles = [todo['title'] for todo in todos if todo['completed'] and todo['userId'] == user_id]
    return titles

def print_report(todos):
    done = completed_count(todos)
    totals = completed_by_user(todos)
    print(f'Loaded: {len(todos)} todos')
    print(f'Completed: {done}')
    print('Completed by user:')
    for userid, count in totals.items():
        print(f'  {userid}: {count}')

    top = top_user(totals)
    print(f'Top user: {top} ({totals[top]} completed)')

todos = fetch_json('https://jsonplaceholder.typicode.com/todos')
print(len(titles_for_user(todos,5)))
print(len(titles_for_user(todos, 1)))


if todos is None:
    print('Could not load data')
else:
    print_report(todos)

