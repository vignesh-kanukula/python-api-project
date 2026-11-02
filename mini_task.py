from helpers import fetch_all
#dict_keys(['users', 'total', 'skip', 'limit'])
# [ X] data shape written as comment
# [X ] plan: in / out / pattern for each function
# [ X] helpers imported, no local copies
# [X ] # Pattern: line on every loop
# [X ] functions use only their parameters
# [x ] if x: only on real True/False; == for text/numbers
# [X ] only print_report prints; test code removed
# [x ] self-check done and passes
# [x ] output read character by character
# [ x] whole file + output in ONE send
# def users by geneder(users) 
#def oldest person(users)
#def avg age(users) 
# def print report(data)

def users_by_gender(users): # GROUP count
    category = {}
    for user in users:
        gender = user['gender']
        if gender in category:
            category[gender] += 1
        else:
            category[gender] = 1
    return category


def oldest_person(users): # BEST SO FAR
    highest_age = 0
    oldest = None
    for user in users:
        age = user['age']
        if age > highest_age:
            highest_age = age
            oldest = user
    return oldest


def average_age(users): # AACUMULATE
    total_age = 0
    for user in users:
       total_age += user['age']
    return total_age / len(users)

def print_report(users):
    print(f"Loaded: {len(users)} users")

    print("Users by gender:")
    category = users_by_gender(users)
    for name, count in category.items():
        print(f"  {name}: {count}")

    checked = sum(category.values())
    if checked == len(users):
        print(f'Check: genders add up to {checked} - OK')
    else:
        print(f'Check: MISMATCH -   users{checked}, users_loaded{len(users)}')

    oldest = oldest_person(users)
    print(f'Oldest: {oldest['firstName']} {oldest['lastName']} ({oldest['age']})')

    average = average_age(users)
    print(f'Average age: {average:.1f}')
    
users = fetch_all('https://dummyjson.com/users', 'users', 50)
if users is None:
    print('Could not load data')
else:
    print_report(users)


