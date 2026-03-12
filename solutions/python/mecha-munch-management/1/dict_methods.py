"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe, items in recipe_updates:
        ideas[recipe] = items
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart alphabetically."""
    sorted_cart = {}
    for key in sorted(cart):
        sorted_cart[key] = cart[key]
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    fulfillment = {}

    # reverse alphabetical order
    for item in sorted(cart.keys(), reverse=True):
        quantity = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        fulfillment[item] = [quantity, aisle, refrigerated]

    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, value in fulfillment_cart.items():
        ordered_quantity = value[0]

        store_quantity, aisle, refrigerated = store_inventory[item]
        remaining = store_quantity - ordered_quantity

        if remaining == 0:
            store_inventory[item] = ['Out of Stock', aisle, refrigerated]
        else:
            store_inventory[item] = [remaining, aisle, refrigerated]

    return store_inventory