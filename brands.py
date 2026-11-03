from helpers import fetch_all
# total product 194
# total missing products 92
# product with brand apple groceries
#<class 'list'>
def brand_counts(products): # GROUP count
    brand_totals = {}
    for product in products:
        brand = product.get('brand', 'No brand')
        if brand in brand_totals:
            brand_totals[brand] += 1
        else:
            brand_totals[brand] = 1
    return brand_totals

def average_price(products):# ACCUMULATE
    total = 0
    for product in products:
        total += product['price']
    return total/len(products)

def by_count(pair):              
    return pair[1]
#
def top_brands(counts, n):    
    pairs = [pair for pair in counts.items() if pair[0] != 'No brand']  
                                
    ordered = sorted(pairs, key=by_count, reverse=True)     
    return ordered[:n]                   

def print_report(products):
    print(f'Loaded: {len(products)} products')

    missing = [p for p in products if p.get('brand') is None]
    print(f'Missing brand: {len(missing)}')

    totals = brand_counts(products)
    print('Top 5 brands:')
    for brand, count in top_brands(totals,5):
        print(f'  {brand}: {count}')

    checked = sum(totals.values())
    if checked == len(products):
        print(f'Check: brands add up to {checked} - OK')
    else:
        print(f'check -  MISMATCHED')


    average = average_price(products)
    print(f'Average price: {average:.2f}')


products = fetch_all('https://dummyjson.com/products', 'products', 100)
if products is None:
    print('Could not load data')
else:
    print_report(products)
