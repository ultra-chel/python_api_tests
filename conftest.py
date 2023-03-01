import pytest
import requests
import random


@pytest.fixture
def get_random_breed():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    list_breeds = [*r.json()['message']]
    random_breed = list_breeds[random.randint(1, len(list_breeds) - 1)]
    return random_breed
