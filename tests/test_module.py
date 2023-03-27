import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code ",
        default="200",
        help="response status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return getattr(requests, request.config.getoption("--status_code"))


def test_status_code(base_url, status_code):
    r = requests.get(base_url)
    assert r == "<Response [{status_code}]>"
