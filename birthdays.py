from helpers import fetch_all
from datetime import datetime


def parse_date(text):
    return  datetime.strptime(text, '%Y-%m-%d')

def births_by_month(users): # GROUP count
    months = {}
    for user in users:
        date = parse_date(user['birthDate'])    
        month = date.strftime('%b')              
        if month in months:
            months[month] += 1
        else:
            months[month] = 1
    return months

def weekend_births(users): # FILTER + COUNT
    weekends = []
    for user in users:
        date = parse_date(user['birthDate'])
        day = date.strftime('%A')
        if day == 'Saturday' or day == 'Sunday':  
             weekends.append(user)
    return weekends

def oldest_by_birth(users):# BEST SO FAR
    oldest_person = None
    oldest_birthday = None
    for user in users:
        date = parse_date(user['birthDate'])
        if oldest_birthday is None or date < oldest_birthday :
            oldest_birthday = date
            oldest_person = user
    return oldest_person


def print_report(users):
    print(f'Loaded: {len(users)} users')

    print('Births by month:')
    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    counts = births_by_month(users)
    for month in MONTHS:
        print(f'  {month}: {counts.get(month, 0)}')
        
    checked = sum(counts.values())
    if checked == len(users):
        print(f'Check: months add up to {checked} - OK')
    else:
        print('Mismatched')

    weekend = weekend_births(users)
    print(f'Born on a weekend: {len(weekend)}')

    oldest = oldest_by_birth(users)
    print(f'Oldest by birth date: {oldest['firstName']} {oldest['lastName']} ({oldest['birthDate']})')

users = fetch_all('https://dummyjson.com/users', 'users', 50)
if users is None:
    print('Could not load data')
else:
    print_report(users)

