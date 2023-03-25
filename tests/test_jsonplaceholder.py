import requests
import pytest
import random
from jsonschema import validate

host = 'https://jsonplaceholder.typicode.com'

json = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}


def test_get_list_posts():
    r = requests.get(host + '/posts')
    schema = {
        "type": "array",
        "properties": {
            "body": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "userId": {"type": "integer"}
        }
    }
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema)


def test_get_one_post(get_random_id_json_placeholder_posts):
    r = requests.get(host + '/posts/' + str(get_random_id_json_placeholder_posts))
    schema = {
        "type": "object",
        "properties": {
            "body": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "userId": {"type": "integer"}
        }
    }
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema)


@pytest.mark.parametrize("incorrect_post_id", [-1, 0, 'null', 555],
                         ids=["negative_int", "zero", 'null', 'non-existent_int'])
def test_get_post_by_incorrect_id(incorrect_post_id):
    schema = {"type": "array"}
    query = {
        'query': incorrect_post_id,
    }
    r = requests.get(host + '/posts/', params=query)
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema)


def test_get_filter_list_by_userid(get_random_userid_json_placeholder_posts):
    userid = get_random_userid_json_placeholder_posts
    r = requests.get(host + '/posts?userId=' + str(userid))
    schema = {
        "type": "array",
        "properties": {
            "body": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "userId": {"type": "integer"}
        }
    }
    assert r.status_code == 200
    for user in r:
        i = 0
        assert r.json()[i]['userId'] == userid
        i += 1
    validate(instance=r.json(), schema=schema)
