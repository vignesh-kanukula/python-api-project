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
