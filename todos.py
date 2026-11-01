
from helpers import fetch_json

def completed_count(todos):# filter + count
    count = 0
    for todo in todos:
        if todo['completed']:
           count += 1
    return count

def completed_by_user(todos): # filter + group
    finished_users = {}
    for todo in todos:
        userid = todo['userId']
        if todo['completed']:
            if userid in finished_users:
                finished_users[userid] += 1
            else:
                finished_users[userid] = 1
    return finished_users

def top_user(totals):# best so far
    highest_user = ''
    highest_total = 0
    for userid, count in totals.items():
        if count > highest_total:
            highest_total = count
            highest_user = userid
    return highest_user
# return first user found
#print(done)
#print(totals)
#print(sum(totals.values()))       # self-check: must equal done
#print(top_user(totals))

#print(len(todos))          # how many items?
#print(todos[0])            # what does ONE item look like?
#print(todos[0].keys())     # what keys can I use?
#print(todos[:3])           # the first 3 items, to see how they vary

def print_report(todos):
    done = completed_count(todos)
    totals = completed_by_user(todos)
    print(f'Loaded: {len(todos)} todos')
    print(f'Completed: {done}')
    print('Completed by user:')
    for userid, count in totals.items():
        print(f'   {userid}: {count}')

    top = top_user(totals)
    print(f'Top user: {top} ({totals[top]} completed)')

todos = fetch_json('https://jsonplaceholder.typicode.com/todos')
if todos is None:
    print('Could not load data')
else:
    print_report(todos)


#todos = fetch_json('https://jsonplaceholder.typicode.com/todos')
#titles = [todo['title'] for todo in todos if todo['completed'] and todo['userId'] ==1 ]
#print(len(titles))      # self-check: must be 11 (user 1's count from Thursday)
#print(titles[0])
