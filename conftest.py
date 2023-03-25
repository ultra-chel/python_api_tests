import pytest
import requests
import random


@pytest.fixture
def get_random_dog_breed():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    list_breeds = [*r.json()['message']]
    return list_breeds[random.randint(1, len(list_breeds) - 1)]


@pytest.fixture
def get_random_brewery_id():
    r = requests.get('https://api.openbrewerydb.org/breweries').json()
    brewery_ids = []
    for brewery in r:
        var = brewery_ids.append(brewery['id'])
    return brewery_ids[random.randint(1, len(brewery_ids) - 1)]


@pytest.fixture
def get_random_brewery_city():
    r = requests.get('https://api.openbrewerydb.org/breweries').json()
    brewery_city = []
    for brewery in r:
        var = brewery_city.append(brewery['city'])
    return brewery_city[random.randint(1, len(brewery_city) - 1)]


@pytest.fixture
def get_random_brewery_country():
    r = requests.get('https://api.openbrewerydb.org/breweries').json()
    brewery_country = []
    for brewery in r:
        var = brewery_country.append(brewery['country'])
    return brewery_country[random.randint(1, len(brewery_country) - 1)]


@pytest.fixture
def get_random_id_json_placeholder_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    posts_ids = []
    for ids in r:
        posts_ids.append(ids['id'])
    return random.choice(posts_ids)


@pytest.fixture
def get_random_userid_json_placeholder_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    user_ids = []
    for ids in r:
        user_ids.append(ids['userId'])
    unique_numbers = list(set(user_ids))
    return random.choice(unique_numbers)
