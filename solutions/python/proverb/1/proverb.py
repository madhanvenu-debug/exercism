def proverb(*items, qualifier=None):
    if not items:
        return []

    result = []

    for first, second in zip(items, items[1:]):
        result.append(f"For want of a {first} the {second} was lost.")

    first_item = items[0]
    if qualifier:
        first_item = f"{qualifier} {first_item}"

    result.append(f"And all for the want of a {first_item}.")

    return result