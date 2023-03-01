import random

import requests
import pytest

host = 'https://api.openbrewerydb.org/'


def test_get_list_breweries_info():
    r = requests.get(host + '/breweries')
    assert r.status_code == 200


def test_get_brewery_info_by_id(get_random_brewery_id):
    r = requests.get(host + '/breweries/' + get_random_brewery_id)
    assert r.status_code == 200


def test_get_brewery_info_by_random():
    r = requests.get(host + '/breweries/random')
    assert r.status_code == 200


def test_get_brewery_info_by_search():
    r = requests.get(host + '/breweries/search')
    assert r.status_code == 200


def test_get_brewery_info_by_metadata():
    r = requests.get(host + '/breweries/meta')
    assert r.status_code == 200
