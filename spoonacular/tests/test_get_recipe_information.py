import random

import pytest
import requests
import logging

from spoonacular.common.common import API_KEY, BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes_complex_search, recipes

logger = logging.getLogger(__name__)


def get_recipe_id() -> int:
    search_string = "Boar"
    recipe_id = None
    url = BASE_URL + recipes_complex_search + "?" + API_KEY + "&query=" + search_string
    response = requests.request("GET", url, headers=HEADERS)
    # handling scenario when no recipes or more than one returned
    if len(response.json()["results"]) == 0:
        recipe_id = 0
    if len(response.json()["results"]) == 1:
        recipe_id = response.json()["results"][0]["id"]
    if len(response.json()["results"]) > 1:
        selected_recipe = random.choice(response.json()["results"])
        recipe_id = selected_recipe["id"]

    return recipe_id

@pytest.mark.all_tests
def test_get_recipe_information() -> None:
    recipe_id = get_recipe_id()
    if recipe_id == 0:
        pytest.skip(logger.info("No recipes found"))
    url = BASE_URL + recipes + "/" + str(recipe_id) + "/" + "information" + "?" + API_KEY
    logger.info("Starting test to get recipe information")
    response = requests.request("GET", url, headers=HEADERS)

    assert response.json()["id"] == recipe_id

    logger.info("Ending test to get recipe information")

#  pytest -m all_tests
#  pytest -s test_get_recipe_information.py::test_get_recipe_information