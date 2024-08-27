"""
why do I have to do this tf, if you read this please explain, would make more sense in the functions itself
"""

import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(original_recipe, num_people):
    dict_recipe = original_recipe.copy()
    amount_more_less_people = num_people / dict_recipe['servings']

    for ingredient, amount in dict_recipe['ingredients'].items():
        dict_recipe['ingredients'][ingredient] = amount * amount_more_less_people

    dict_recipe['servings'] = num_people
    return dict_recipe


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4} '
    # Dein Code kommt hier hin
