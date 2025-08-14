import pytest
import requests
import logging

from spoonacular.common.common import API_KEY, BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes_complex_search

logger = logging.getLogger(__name__)

# https://api.spoonacular.com/ recipes/complexSearch ? apiKey=4efb4de578084b1c84736d320c5ef279 & query=Apple

# Search through recipes
@pytest.mark.all_tests
def test_search():
    search_string = "Apple"
    url = BASE_URL + recipes_complex_search + "?" + API_KEY + "&" + search_string
    logger.info(f"Starting search for {search_string} test")
    response = requests.request("GET", url, headers=HEADERS)
    print(response.json())

    logger.info(f"Ending search for {search_string} test")

#  pytest -m all_tests
#  pytest -s test_search_recipes.py::test_search