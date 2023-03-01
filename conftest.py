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
