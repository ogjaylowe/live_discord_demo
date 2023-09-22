import pytest
from utils.managers import send_get_request


def test_get_request(_root_url):
    response = send_get_request(f"{_root_url}/get-data")
    response = send_get_request()

    # Check the response status code
    assert response.status_code == 200, "response not 200 -- issue with request"
    # If the response is successful (status code 200), parse the JSON data
    data = response.json()

    print("Data received:")
    print(data)


def test_form_polygon_request(_root_url):
    return 1


def test_send_polygon_request(_root_url):
    return 1


def test_requesting_random_words():
    return 1


def test_random_words_logic():
    return 1
