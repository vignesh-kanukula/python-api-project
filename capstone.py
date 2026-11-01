from helpers import fetch_json
#<class 'dict'>
#dict_keys(['recipes', 'total', 'skip', 'limit'])
#           list        int       int     int
#data{ receipes [ recepie { ingredients [ ingredient
#     loop1               loop2 
# def recipes by cusine(recipes) pattern : Group count
# def recepie difficulty(recipes)  pattern : filter+ count
#def top rated(recipes)pattern: best so far
#def avg calories(recipes)pattern accumulate
#def tags_by_recipe(recipes):# GROUP
#def common tag(totals))pattern: best so far
# [ X] data shape written as comment
# [X] plan: in / out / pattern for each function
# [ X] helpers imported, no local copies
# [X ] # Pattern: line on every loop
# [X ] functions use only their parameters
# [ ] no variable named after a key
# [ x] if x: only on real True/False; == for text/numbers
# [X ] only print_report prints; test code removed
# [x ] self-check done and passes
# [ ] output read character by character
# [x ] whole file + output in ONE send
def recipes_by_cuisine(recipes): # GROUP count
    style = {}
    for recipe in recipes:
        cuisine = recipe['cuisine']
        if cuisine in style:
            style[cuisine] += 1
        else:
            style[cuisine] = 1
    return style

def recipe_difficulty(recipes): # FILTER + COUNT
    total = 0
    for recipe in recipes:
        if recipe['difficulty'] == 'Easy':
            total += 1
    return total

def top_rated(recipes): # BEST SO FAR
    highest_rating = 0
    best_recipe = None
    for recipe in recipes:
        if recipe['rating'] > highest_rating:
            highest_rating = recipe['rating']
            best_recipe = recipe
    return best_recipe

def avgerage_calories(recipes): # ACCUMULATE
    count = 0
    for recipe in recipes:
        count += recipe['caloriesPerServing']       
    return count/len(recipes)

def tags_by_recipe(recipes):# GROUP
    totals = {}
    for recipe in recipes:
        for tag in recipe['tags']:
            if tag in totals:
                totals[tag] += 1
            else:
                totals[tag] = 1
    return totals

def common_tag(totals): # BEST SO FAR
    best_tag = None
    best_tag_total = 0
    for tag, count in totals.items():
        if count > best_tag_total:
            best_tag_total = count
            best_tag = tag
    return best_tag


def print_report(data):
    recipes = data['recipes']
    totals = tags_by_recipe(recipes)
    print(f"Loaded: {len(recipes)} recipes (of {data['total']} total)")
    print('Recipes by cuisine:')
    style = recipes_by_cuisine(recipes)
    for name, count in style.items():
        print(f'  {name}: {count}')

    checked = sum(style.values())
    if  checked == len(recipes):
        print(f'Check: cuisines add up to {checked} - OK')
    else:
        print(f'Check: MISMATCH -   cuisines{checked}, recipes {len(recipes)}')

    easy = recipe_difficulty(recipes)
    print(f'Easy recipes: {easy}')

    best_rating = top_rated(recipes)

    print(f"Top rated: {best_rating['name']}({best_rating['rating']}) ")

    counts = avgerage_calories(recipes)
    print(f'Average calories: {counts:.1f}')

    best = common_tag(totals)
    print(f'Most common tag: {best} ({totals[best]} recipes) ')


data = fetch_json('https://dummyjson.com/recipes')
if data is None:
    print("Could not load the data.")
else:
    print_report(data)

#1. READ. Read the whole hint once, hands off the keyboard.
#2. PASTE. Copy it into your file as numbered checkboxes:

#python
# HINT 2
# [ ] 1. replace check block with sum(style.values())
# [ ] 2. top_rated returns the whole recipe + print the rating
# [ ] 3. tag line: add totals[best] + "recipes"

#3. ONE AT A TIME. Do item 1, tick it, then item 2. Never two at once.
#4. RE-READ. Before you run the code, read the hint once more against your code.