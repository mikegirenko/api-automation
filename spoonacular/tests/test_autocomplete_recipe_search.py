import pytest
import requests
import logging

from spoonacular.test_data.hardcoded import API_KEY
from spoonacular.namespace_urls.namespace_urls import BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes_autocomplete

logger = logging.getLogger(__name__)


@pytest.mark.all_tests
def test_autocomplete_recipe_search() -> None:
    logger.info(
        "Starting test which autocompletes a partial input to suggest possible recipe names"
    )

    query_to_be_autocompleted = "chick"
    number_of_results_to_return = 10
    url = (
        BASE_URL
        + recipes_autocomplete
        + "?number="
        + str(number_of_results_to_return)
        + "&query="
        + query_to_be_autocompleted
        + "&"
        + API_KEY
    )
    response = requests.request("GET", url, headers=HEADERS, verify=False)

    logger.info("Confirm response has 10 or less recipes")
    assert len(response.json()) <= number_of_results_to_return

    logger.info("Confirm for each returned recipe 'title' field has 'chick'")
    for recipe in response.json():
        assert "chick" in recipe["title"]

    logger.info("Confirm first returned recipe's 'title' field has 'chicken'")
    assert "chicken" in response.json()[0]["title"]
