"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from dish_ingredients."""
    
    ingredient_set = set(dish_ingredients)
    return (dish_name, ingredient_set)


def check_drinks(drink_name, drink_ingredients):
    """Append Cocktail or Mocktail depending on alcohol presence."""
    
    ingredient_set = set(drink_ingredients)

    if ingredient_set.intersection(ALCOHOLS):
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredients."""
    
    if dish_ingredients.issubset(VEGAN):
        category = "VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif dish_ingredients.issubset(KETO):
        category = "KETO"
    elif dish_ingredients.issubset(PALEO):
        category = "PALEO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Return special ingredients used in the dish."""
    
    dish_name, dish_ingredients = dish
    special = set(dish_ingredients).intersection(SPECIAL_INGREDIENTS)

    return (dish_name, special)


def compile_ingredients(dishes):
    """Create master ingredient list."""
    
    master_set = set()

    for dish in dishes:
        master_set = master_set.union(dish)

    return master_set


def separate_appetizers(dishes, appetizers):
    """Remove appetizers from dishes."""
    
    dish_set = set(dishes)
    appetizer_set = set(appetizers)

    result = dish_set.difference(appetizer_set)

    return list(result)


def singleton_ingredients(dishes, intersection):
    """Find ingredients that appear in only one dish."""
    
    all_ingredients = set()
    duplicates = set()

    for dish in dishes:
        for ingredient in dish:
            if ingredient in all_ingredients:
                duplicates.add(ingredient)
            else:
                all_ingredients.add(ingredient)

    singleton = all_ingredients - duplicates
    singleton = singleton - intersection

    return singleton