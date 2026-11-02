import requests


def fetch_json(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return None
    if response.status_code != 200:
        return None
    return response.json()


def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None

def fetch_all(base_url, key, page_size):      # Pattern: ACCUMULATE (pages)
    items = []
    skip = 0
    while True:
        data = fetch_json(f'{base_url}?limit={page_size}&skip={skip}')
        if data is None:
            return None
        items.extend(data[key])          
        skip += page_size   
        if skip >= data['total']:     
            break
    return items