import requests
import pytest
import random
from jsonschema import validate
import string

host = 'https://jsonplaceholder.typicode.com'


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


schema_one_post = {
    "type": "object",
    "properties": {
        "body": {"type": "string"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "userId": {"type": "integer"}
    }
}

schema_list_posts = {
        "type": "array",
        "properties": {
            "body": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "userId": {"type": "integer"}
        }
    }


def test_get_list_posts():
    r = requests.get(host + '/posts')
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema_list_posts)


def test_get_one_post(get_random_id_json_placeholder_posts):
    r = requests.get(host + '/posts/' + str(get_random_id_json_placeholder_posts))
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema_one_post)


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
    assert r.status_code == 200
    for user in r:
        i = 0
        assert r.json()[i]['userId'] == userid
        i += 1
    validate(instance=r.json(), schema=schema_list_posts)


@pytest.mark.parametrize("length_cases",
                         [generate_random_string(9), generate_random_string(55), generate_random_string(105)],
                         ids=["string 1-9 symbols", "string 10-99 symbols", 'string >100 symbols'])
def test_positive_create_post(length_cases):
    json = {
        'title': 'foo',
        'body': length_cases,
        'userId': 1,
    }
    r = requests.post(url=host + '/posts',
                      headers={
                          'Content-type': 'application/json; charset=UTF-8',
                      },
                      json=json)
    assert r.status_code == 201
    assert r.json()['body'] == length_cases
    validate(instance=r.json(), schema=schema_one_post)
