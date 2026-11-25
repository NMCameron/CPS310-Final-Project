"""Tests for the starter Recipe & Meal Planner."""

import json

from recipe_utils import filter_by_category, load_config, load_recipes, search_by_name, favorite_recipe


def test_search_by_name_finds_partial_match():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "chicken")
    assert result == [{"name": "Chicken Alfredo", "category": "Dinner"}]


def test_search_by_name_is_case_insensitive():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "SMOOTHIE")
    assert result == [{"name": "Berry Smoothie", "category": "Snack"}]


def test_search_by_name_returns_empty_list_when_no_match():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert search_by_name(recipes, "pizza") == []


def test_filter_by_category_returns_matching_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": ["Dinner"]},
        {"name": "Berry Smoothie", "category": ["Snack"]},
        {"name": "Tomato Pasta", "category": ["Dinner"]},
    ]
    result = filter_by_category(recipes, "Dinner")
    assert result == [
        {"name": "Chicken Alfredo", "category": ["Dinner"]},
        {"name": "Tomato Pasta", "category": ["Dinner"]},
    ]


def test_filter_by_category_is_case_insensitive():
    recipes = [{"name": "Chicken Alfredo", "category": ["Dinner"]}]
    assert filter_by_category(recipes, "dinner") == [
        {"name": "Chicken Alfredo", "category": ["Dinner"]}
    ]


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "app_title": "Test Planner",
                "recipe_file": "recipes.json",
                "default_servings": 2,
            }
        ),
        encoding="utf-8",
    )
    result = load_config(config_file)
    assert result["app_title"] == "Test Planner"
    assert result["default_servings"] == 2


def test_load_recipes_reads_json(tmp_path):
    recipe_file = tmp_path / "recipes.json"
    sample = [
        {
            "name": "Test Recipe",
            "category": "Lunch",
            "servings": 2,
            "prep_time": 5,
            "cook_time": 10,
            "ingredients": [],
        }
    ]
    recipe_file.write_text(json.dumps(sample), encoding="utf-8")
    assert load_recipes(recipe_file) == sample

def test_favorite_recipe_adds_favorite_category():
    recipes = [{"name": "Chicken Alfredo", "category": ["Dinner"]}]
    result = favorite_recipe(recipes, 1)
    assert result == True
    assert recipes[0]["category"] == ["Dinner", "Favorite"]


def test_favorite_recipe_prevents_duplicates():
    recipes = [{"name": "Chicken Alfredo", "category": ["Dinner", "Favorite"]}]
    result = favorite_recipe(recipes, 1)
    assert result == False
    assert recipes[0]["category"].count("Favorite") == 1


def test_favorite_recipe_rejects_invalid_selection():
    recipes = [{"name": "Chicken Alfredo", "category": ["Dinner"]}]
    result = favorite_recipe(recipes, 2)
    assert result == False
    assert recipes[0]["category"] == ["Dinner"]


def test_filter_by_category_returns_favorite_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": ["Dinner", "Favorite"]},
        {"name": "Berry Smoothie", "category": ["Snack"]},
        {"name": "Tomato Pasta", "category": ["Dinner", "Favorite"]},
    ]
    result = filter_by_category(recipes, "Favorite")
    assert result == [recipes[0], recipes[2]]


def test_filter_by_category_returns_empty_favorites():
    recipes = [
        {"name": "Chicken Alfredo", "category": ["Dinner"]},
        {"name": "Berry Smoothie", "category": ["Snack"]},
    ]
    result = filter_by_category(recipes, "Favorite")
    assert result == []
