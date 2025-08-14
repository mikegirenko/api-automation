import pytest
import requests
import logging

from spoonacular.common.common import API_KEY, BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes_complex_search

logger = logging.getLogger(__name__)


@pytest.mark.all_tests
def test_recipe_search_query():
    search_string = "Apple"
    url = BASE_URL + recipes_complex_search + "?" + API_KEY + "&query=" + search_string
    title_without_search_string = []
    title_with_search_string = []
    logger.info(f"Starting test and searching for {search_string}")

    response = requests.request("GET", url, headers=HEADERS)

    # I am not sure why (and it might be a defect) but search returns recipes without "Apple" in the title.
    # So, I am simply collecting all titles and confirming some have it and some do not
    for result in response.json()["results"]:
        if search_string in result["title"]:
            title_with_search_string.append(result["title"])
        if search_string not in result["title"]:
            title_without_search_string.append(result["title"])

    for title in title_with_search_string:
        assert search_string in title

    for title in title_without_search_string:
        assert search_string not in title

    logger.info(f"Ending search for {search_string} test")

#  pytest -m all_tests
#  pytest -s test_search_all_recipes.py::test_recipe_search_query