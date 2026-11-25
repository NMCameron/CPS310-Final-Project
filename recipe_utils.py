"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if category in [tag.lower() for tag in recipe["category"]]
    ]


def favorite_recipe(recipes, recipe_number):
    """Add the Favorite category to a selected recipe."""
    if recipe_number < 1 or recipe_number > len(recipes):
        return False

    recipe = recipes[recipe_number - 1]

    if "Favorite" in recipe["category"]:
        return False

    recipe["category"].append("Favorite")
    return True