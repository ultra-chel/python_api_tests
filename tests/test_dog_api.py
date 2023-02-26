import requests
import pytest

host = 'https://dog.ceo/api'


def test_get_list_dog_breeds():
    r = requests.get(host + '/breeds/list/all')
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


def test_get_random_dog_breeds_image():
    r = requests.get(host + '/breeds/image/random')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    # схему проверить


def test_get_dog_breeds_list_images():
    r = requests.get(host + '/api/breed/hound/images')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    # параметризация породы
    # схему проверить
