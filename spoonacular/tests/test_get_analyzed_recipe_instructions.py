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
def test_get_analyzed_recipe_instructions() -> None:
    logger.info(
        "Starting test to get an analyzed breakdown of a recipe's instructions."
    )
    recipe_id = (
        1095791  # get_recipe_id("Apple")  # remember that this returns random recipe_id
    )
    if recipe_id == 0:
        pytest.skip(logger.info("No recipes found"))

    url = (
        BASE_URL
        + recipes
        + "/"
        + str(recipe_id)
        + "/"
        + "analyzedInstructions"
        + "?"
        + API_KEY
    )
    response = requests.request("GET", url, headers=HEADERS, verify=False)
    steps = response.json()[0]["steps"]

    logger.info("Confirm response has steps.")
    assert len(response.json()) > 0

    one_step = steps[0]  # hardcoding 0 for now, may need to change in the future

    logger.info("Confirm step has title.")
    step = one_step["step"]
    assert len(step) > 0
    assert step.isprintable()

    logger.info("Confirm step has equipment node.")
    equipment = one_step["equipment"]
    for individual_equipment in equipment:
        assert "id" in individual_equipment
        assert "name" in individual_equipment
        assert "localizedName" in individual_equipment
        assert "image" in individual_equipment

    logger.info("Confirm step has ingredients node.")
    ingredients = one_step["ingredients"]
    for individual_ingredient in ingredients:
        assert "id" in individual_ingredient
        assert "name" in individual_ingredient
        assert "localizedName" in individual_ingredient
        assert "image" in individual_ingredient
