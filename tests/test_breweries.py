import random

import requests
import pytest

host = 'https://api.openbrewerydb.org/'


def test_get_list_breweries():
    r = requests.get(host + '/breweries')

    assert r.status_code == 200
    assert r.json()['status'] == "success"


@pytest.mark.parametrize("breeds", ['borzoi', 'hound', 'fakebreed'], ids=["empty_sub_breed", "sub_breed", "fakebreed"])
def test_get_list_dog_sub_breeds(breeds):
    r = requests.get(host + '/breed/' + breeds + '/list')
    if breeds == 'fakebreed':
        assert r.status_code == 404
    else:
        assert r.status_code == 200
        assert r.json()['status'] == "success"
    # параметризация породы


def test_get_random_all_dog_breeds_image():
    r = requests.get(host + '/breeds/image/random')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    # схему проверить


def test_get_dog_breeds_list_images():
    r = requests.get(host + '/breed/hound/images')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    # параметризация породы
    # схему проверить



@pytest.mark.parametrize("breed", random_breed, ids=random_breed)
def test_get_random_define_dog_breeds_image(breed):
    print(breed)
    r = requests.get(host + '/breed/' + breed + '/images/random')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    # параметризация породы
    # схему проверить
    # разобраться как рандомную породу пихать каждый новый тест
