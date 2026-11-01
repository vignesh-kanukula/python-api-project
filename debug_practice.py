staff = [
    {'name': 'ann', 'shifts': [{'day': 'mon', 'hours': 8}, {'day': 'tue', 'hours': 6}]},
    {'name': 'bo',  'shifts': [{'day': 'mon', 'hours': 4}]},
    {'name': 'cy',  'shifts': [{'day': 'wed', 'hours': 10}, {'day': 'thu', 'hours': 2}]},
]

def hours_for(person):
    total = 0
    for shift in person['shifts']:
        total += shift['hours']
    return total

def hours_by_person(staff):
    result = {}
    for person in staff:
        result[person['name']] = hours_for(person)
    return result

def busiest(totals):
    best_name = ''
    best_hours = 0
    for name, hours in totals.items():
        if hours > best_hours:
            best_hours = hours
            best_name = name
    return best_name

totals = hours_by_person(staff)
print(totals)
print(busiest(totals))