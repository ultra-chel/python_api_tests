import requests
from jsonschema import validate
import pytest

from conftest import get_random_brewery_city, get_random_brewery_country

host = 'https://api.openbrewerydb.org/v1'

schema_breweries_info = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": ["string", "null"]},
        "address_1": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    },
    "required": ["id", "name", "brewery_type"]
}

schema_random_breweries_info = {
    "type": "array",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": ["string", "null"]},
        "address_1": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"}
    },
    "required": ["id", "name", "brewery_type"]
}


def test_get_list_breweries_info():
    r = requests.get(host + '/breweries')
    assert r.status_code == 200


def test_get_brewery_info_by_id(get_random_brewery_id):
    r = requests.get(host + '/breweries/' + get_random_brewery_id)
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema_breweries_info)


def test_get_brewery_info_by_random():
    r = requests.get(host + '/breweries/random')
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema_random_breweries_info)


@pytest.mark.parametrize("search_params", [get_random_brewery_city, get_random_brewery_country],
                         ids=["search_by_city", "search_by_country"])
def test_get_brewery_info_by_search(search_params):
    query = {
        'query': search_params,
        'per_page': '3'
    }
    r = requests.get(host + '/breweries/search', params=query)
    assert r.status_code == 200


@pytest.mark.parametrize("types", ["micro", "large", "brewpub", "closed"])
def test_get_breweries_metadata_by_type(types):
    schema_breweries_meta = {
        "type": "object",
        "properties": {
            "total": {"type": "string"},
            "page": {"type": "string"},
            "per_page": {"type": "string"},
        },
        "required": ["total", "page", "per_page"]
    }
    query = {
        'by_type': types,
        'per_page': '3'
    }
    r = requests.get(host + '/breweries/meta', params=query)
    assert r.status_code == 200
    validate(instance=r.json(), schema=schema_breweries_meta)
