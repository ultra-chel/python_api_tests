import requests
import pytest
from jsonschema import validate

host = 'https://dog.ceo/api'


def test_get_list_dog_breeds():
    r = requests.get(host + '/breeds/list/all')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    validate(instance=r.json(), schema=schema)


@pytest.mark.parametrize("breeds", ['borzoi', 'hound', 'fakebreed'], ids=["empty_sub_breed", "sub_breed", "fakebreed"])
def test_get_list_dog_sub_breeds(breeds):
    r = requests.get(host + '/breed/' + breeds + '/list')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    if breeds == 'fakebreed':
        assert r.status_code == 404
    else:
        assert r.status_code == 200
        assert r.json()['status'] == "success"
        validate(instance=r.json(), schema=schema)


def test_get_random_all_dog_breeds_image():
    r = requests.get(host + '/breeds/image/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    validate(instance=r.json(), schema=schema)


@pytest.mark.parametrize("breeds", ['borzoi', 'hound', 'fakebreed'], ids=["empty_sub_breed", "sub_breed", "fakebreed"])
def test_get_dog_breeds_list_images(breeds):
    r = requests.get(host + '/breed/' + breeds + '/images')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    if breeds == 'fakebreed':
        assert r.status_code == 404
    else:
        assert r.status_code == 200
        assert r.json()['status'] == "success"
        validate(instance=r.json(), schema=schema)


def test_get_random_define_dog_breeds_image(get_random_dog_breed):
    r = requests.get(host + '/breed/' + get_random_dog_breed + '/images/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    validate(instance=r.json(), schema=schema)
