from helpers import fetch_json
import json

# [ X] data shape written as comment
# [X ] plan: in / out / pattern for each function
# [ X] helpers imported, no local copies
# [X ] # Pattern: line on every loop
# [X ] functions use only their parameters
# [ ] no variable named after a key
# [ ] if x: only on real True/False; == for text/numbers
# [X ] only print_report prints; test code removed
# [ ] self-check done and passes
# [ ] output read character by character
# [ ] whole file + output in ONE send
# shape dict, len == 4
#dict_keys(['products', 'total', 'skip', 'limit'])
#{products: list, total: int, skip: int, limit: int}
# data { products [ product { reviews [ review { rating
#       loop 1               loop2
#len products == 30
#{'id': 1, 'title': 'Essence Mascara Lash Princess', 'description': 'The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.', 'category': 'beauty', 'price': 9.99, 'discountPercentage': 10.48, 'rating': 2.56, 'stock': 99, 'tags': ['beauty', 'mascara'], 'brand': 'Essence', 'sku': 'BEA-ESS-ESS-001', 'weight': 4, 'dimensions': {'width': 15.14, 'height': 13.08, 'depth': 22.99}, 'warrantyInformation': '1 week warranty', 'shippingInformation': 'Ships in 3-5 business days', 'availabilityStatus': 'In Stock', 'reviews': [{'rating': 3, 'comment': 'Would not recommend!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Eleanor Collins', 'reviewerEmail': 'eleanor.collins@x.dummyjson.com'}, {'rating': 4, 'comment': 'Very satisfied!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Lucas Gordon', 'reviewerEmail': 'lucas.gordon@x.dummyjson.com'}, {'rating': 5, 'comment': 'Highly impressed!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Eleanor Collins', 'reviewerEmail': 'eleanor.collins@x.dummyjson.com'}], 'returnPolicy': 'No return policy', 'minimumOrderQuantity': 48, 'meta': {'createdAt': '2025-10-09T14:47:01.588Z', 'updatedAt': '2026-05-23T11:27:41.868Z', 'barcode': '5784719087687', 'qrCode': 'https://cdn.dummyjson.com/public/qr-code.png'}, 'images': ['https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp'], 'thumbnail': 'https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp'}
#dict_keys(['id', 'title', 'description', 'category', 'price', 'discountPercentage', 'rating', 'stock', 'tags', 'brand', 'sku', 'weight', 'dimensions', 'warrantyInformation', 'shippingInformation', 'availabilityStatus', 'reviews', 'returnPolicy', 'minimumOrderQuantity', 'meta', 'images', 'thumbnail']data = fetch_json('https://dummyjson.com/products')
# id, title, .....thumbnail --- level 1
# tags --- list
# dimensions --- dict
# reviews --- list---- level 2
#       rating : 3, comment ----dict ---level 
#       rating : 4, ---dict ----level 
#       rating : 5,  dict---- level 
# meta -- dict----- level 2
#images ---- list

# plan 
#def products category(products) in : products /out : product count patteren: Group Count
# def low stock(products) in: products  / out : number of low products pattern: filter + count
# def most expensive(products) in : products/ out: single product pattern: best so far
# def total reviews(products) in : products/ out : total reviews number pattern: accumulate
# def 5 star reviews(products) in :products/out: total 5 star number pattern : filter + count
def products_by_category(products): # GROUP count
    counts  = {}
    for product in products:
        category_name = product['category']
        if category_name in counts:
            counts[category_name] += 1
        else:
            counts[category_name] = 1
    return counts

def by_count(pair):
    return pair[1]

def most_expensive(products): # BEST SO FAR
    best_product = None
    best_price  = 0
    for product in products:
        amount = product['price']
        if amount > best_price:
            best_price = amount
            best_product = product
    return best_product

def low_stock(products): # FILTER + COUNT
    low_products = [product for product in products if product['stock'] < 10]

    return len(low_products)


def total_reviews(products): # ACCUMULATE
    total = 0
    for product in products:
        total += len(product['reviews'])
    return total

def five_star_reviews(products): # FILTER + COUNT
    count = 0
    for product in products:
        for review in product['reviews']:
           if review['rating'] == 5:
            count += 1
    return count

def build_summary(products):
    winner = most_expensive(products)
    return{
        'loaded': len(products),
        'by_category': products_by_category(products),
        'most_expensive': winner['title'],
    }

def save_json(summary, path):                    
    with open(path, 'w') as file:
        json.dump(summary, file, indent=2)

def print_report(data):
    products = data['products']
    print(f"Loaded: {len(products)} products (of {data['total']} total)")

    print(f'Products by category:')
    counts = products_by_category(products)
    for name, count in counts.items():
       print(f'  {name}: {count}')
    print(sorted(counts.items(), key=by_count, reverse = True))

    checked = sum(counts.values())                   # add up all categories
    if checked == len(products):
        print(f'Check: categories add up to {checked} - OK')
    else:
        print(f'Check: MISMATCH - categories {checked}, products {len(products)}')

    under_stock = low_stock(products)
    print(f'Low stock (under 10): {under_stock} products')

    winner = most_expensive(products)
    print(f"Most expensive: {winner['title']} ({winner['price']:.2f})")

    count = total_reviews(products)
    print(f'Total reviews: {count}') 

    five_star_count = five_star_reviews(products)
    print(f'5-star reviews: {five_star_count}')

data = fetch_json('https://dummyjson.com/products')



if data is None:
    print('Could not load data')
else:
    print_report(data)
    summary = build_summary(data['products'])
    save_json(summary,'reads/report.json')

import json
with open('reads/report.json') as file:
    print(json.load(file))

