import requests

BASE_URL = 'http://localhost:5000'


def add_book(book_data):
    response = requests.post(f'{BASE_URL}/books', json=book_data)
    return response.json()


def add_categories(categories_data):
    response = requests.post(f'{BASE_URL}/categories', json=categories_data)
    return response.json()
