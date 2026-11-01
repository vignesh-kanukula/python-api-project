from helpers import fetch_json, safe_float

# <class 'dict'>
# dict_keys(['carts', 'total', 'skip', 'limit'])
#{'id': 1, 'products': [{'id': 162, 'title': 'Blue Frock', 'price': 29.99, 'quantity': 4, 'total': 119.96, 'discountPercentage': 12.13, 'discountedTotal': 105.41, 'thumbnail': 'https://cdn.dummyjson.com/product-images/tops/blue-frock/thumbnail.webp'}, {'id': 113, 'title': 'Generic Motorcycle', 'price': 3999.99, 'quantity': 3, 'total': 11999.97, 'discountPercentage': 12.1, 'discountedTotal': 10547.97, 'thumbnail': 'https://cdn.dummyjson.com/product-images/motorcycle/generic-motorcycle/thumbnail.webp'}, {'id': 122, 'title': 'iPhone 6', 'price': 299.99, 'quantity': 3, 'total': 899.97, 'discountPercentage': 6.69, 'discountedTotal': 839.76, 'thumbnail': 'https://cdn.dummyjson.com/product-images/smartphones/iphone-6/thumbnail.webp'}, {'id': 138, 'title': 'Baseball Ball', 'price': 8.99, 'quantity': 2, 'total': 17.98, 'discountPercentage': 1.71, 'discountedTotal': 17.67, 'thumbnail': 'https://cdn.dummyjson.com/product-images/sports-accessories/baseball-ball/thumbnail.webp'}], 'total': 13037.88, 'discountedTotal': 11510.81, 'userId': 1, 'totalProducts': 4, 'totalQuantity': 12}
#  data{ carts [ cart { products [ product {
#      loop 1          loop 2
# def total_value(carts) pattern: accmulate in: carts out: total
# def biggest cart(carts) pattern: best so far in: carts out : best cart
# def carts over(carts) pattern: filter + count in: carts out: single number
# def unitssold(carts) pattern : accumulate in: carts out: total
# def unitsbycart(carts) pattern : group count in: carts out: count
# def topproduct(totals) pattern : best so far in: totals out: top product
# [ X] data shape written as comment
# [X] plan: in / out / pattern for each function
# [ X] helpers imported, no local copies
# [X ] # Pattern: line on every loop
# [X ] functions use only their parameters
# [ ] no variable named after a key
# [ x] if x: only on real True/False; == for text/numbers
# [X ] only print_report prints; test code removed
# [x ] self-check done and passes
# [x ] output read character by character
# [x ] whole file + output in ONE send

def total_value(carts): # ACCUMULATE
    total = 0
    for cart in carts:
        total += cart['total']
    return total

def biggest_cart(carts): # BEST SO FAR
    highest_cart = 0
    best_cart = None
    for cart in carts:
        total = safe_float(cart['total'])
        if total > highest_cart:
            highest_cart = total
            best_cart = cart
    return best_cart

def cart_quantity_total(carts):        # Pattern: ACCUMULATE
    total = 0
    for cart in carts:
        total += cart['totalQuantity']
    return total

def carts_over10000(carts): # FILTER + COUNT
    big_carts = []
    for cart in carts:
        total = cart['total']
        if total > 10000:
            big_carts.append(cart)
    return len(big_carts)

def units_sold(carts): # ACCUMULATE
    total = 0
    for cart in carts:
        for product in cart['products']:
            total += product['quantity']
    return total

def units_by_products(carts): # GROUP total
    totals = {}
    for cart in carts:
        for product in cart['products']:
            name = product['title']
            if name in totals:
                totals[name] += product['quantity']
            else: 
                totals[name] = product['quantity']
    return totals

def top_product(totals): # BEST SO FAR
    best_product = None
    best_total = 0
    for product, total in totals.items():
        if total > best_total:
            best_total = total
            best_product = product
    return best_product

def print_report(data):
    carts = data['carts']
    totals = units_by_products(carts)
    print(f'Loaded: {len(carts)} carts (of {data['total']} total)')

    total = total_value(carts)
    print(f'Total value: {total:.2f}')

    winner = biggest_cart(carts)
    print(f"Biggest cart: #{winner['id']} for user {winner['userId']} ({winner['total']:.2f})")

    highest_carts = carts_over10000(carts)
    print(f'Carts over 10000: {highest_carts}')

    sold = units_sold(carts)
    print(f'Units sold: {sold}')

    expected = cart_quantity_total(carts)
    if sold == expected:
        print('Check: units match cart totals - OK')
    else:
        print(f'Check: MISMATCH - products {sold}, carts {expected}')
       
    top = top_product(totals)
    print(f'Top product: {top} ({totals[top]} units)')


data = fetch_json('https://dummyjson.com/carts')
if data is None:
    print('Could not load data')
else:
    print_report(data)
  