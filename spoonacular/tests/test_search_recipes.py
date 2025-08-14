import pytest
import requests

from spoonacular.common.common import API_KEY, BASE_URL
from spoonacular.request.headers import HEADERS


# Search through thousands of recipes using advanced filtering and ranking

def test_search():
    URL = BASE_URL + "recipes/complexSearch?query=" + "Apple" + API_KEY
    response = requests.request("GET", URL, headers=HEADERS)
    print(response.json())
