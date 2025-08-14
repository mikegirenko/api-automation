import pytest
import requests
import logging

from spoonacular.common.common import API_KEY, BASE_URL
from spoonacular.request.headers import HEADERS

logger = logging.getLogger(__name__)

# Search through recipes
@pytest.mark.all_tests
def test_search():
    logger.info("Starting search test")
    URL = BASE_URL + "recipes/complexSearch?query=" + "Apple" + API_KEY
    response = requests.request("GET", URL, headers=HEADERS)
    print(response.json())

    logger.info("Ending search test")

#  pytest -m all_tests
#  pytest -s test_search_recipes.py::test_search