"""
functions to perform user actions
 answer_something()
"""
import random

import requests
import logging
from spoonacular.namespace_urls.namespace_urls import BASE_URL
from spoonacular.request.headers import HEADERS
from spoonacular.request.query import recipes_complex_search
from spoonacular.test_data.hardcoded import API_KEY

logger = logging.getLogger(__name__)


def get_recipe_id(search_string) -> int:
    recipe_id = None
    url = BASE_URL + recipes_complex_search + "?" + API_KEY + "&query=" + search_string
    response = requests.request("GET", url, headers=HEADERS, verify=False)
    # handling scenario when no recipes or more than one returned
    if len(response.json()["results"]) == 0:
        recipe_id = 0
    if len(response.json()["results"]) == 1:
        recipe_id = response.json()["results"][0]["id"]
    if len(response.json()["results"]) > 1:
        selected_recipe = random.choice(response.json()["results"])
        recipe_id = selected_recipe["id"]

    logger.info(f"Recipe id is {recipe_id}")

    return recipe_id