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
def test_get_recipe_taste() -> None:
    logger.info("Starting test to get a recipe's taste.")
    recipe_id = get_recipe_id("Apple")
    if recipe_id == 0:
        pytest.skip(logger.info("No recipes found"))
    url = BASE_URL + recipes + "/" + str(recipe_id) + "/" + "tasteWidget.json" + "?" + API_KEY

    response = requests.request("GET", url, headers=HEADERS, verify=False)

    logger.info("Confirm response has all seven tastes.")
    assert len(response.json()) == 7

    logger.info("Confirm tastes are between 0 and 100 while the spiciness value is an open scale of 0 and above.")
    for k, v in response.json().items():
        if k == "spiciness":
            assert v >= 0
        else:
            assert 0 <= v <= 100

    logger.info("Ending test to get a recipe's taste.")
