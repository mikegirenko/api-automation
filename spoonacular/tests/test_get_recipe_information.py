import random

import pytest
import requests
import logging

from spoonacular.test_data.hardcoded import API_KEY
from spoonacular.namespace_urls.namespace_urls import BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes
from spoonacular.user_api_abstraction.user_api_abstraction import get_recipe_id

logger = logging.getLogger(__name__)


@pytest.mark.all_tests
def test_get_recipe_information() -> None:
    logger.info("Starting test to get recipe information")
    recipe_id = get_recipe_id("Boar")
    if recipe_id == 0:
        pytest.skip(logger.info("No recipes found"))
    url = BASE_URL + recipes + "/" + str(recipe_id) + "/" + "information" + "?" + API_KEY

    response = requests.request("GET", url, headers=HEADERS, verify=False)

    assert response.json()["id"] == recipe_id

    logger.info("Ending test to get recipe information")

#  pytest -m all_tests
#  pytest -s test_get_recipe_information.py::test_get_recipe_information