"""Implement basic list operations."""


def append(list1, list2):
    """Append two lists."""
    result = []

    for item in list1:
        result.append(item)

    for item in list2:
        result.append(item)

    return result


def concat(lists):
    """Concatenate a list of lists."""
    result = []

    for current_list in lists:
        result = append(result, current_list)

    return result


def filter(function, items):
    """Filter items using a function."""
    result = []

    for item in items:
        if function(item):
            result.append(item)

    return result


def length(items):
    """Return the length of a list."""
    count = 0

    for item in items:
        count += 1

    return count


def map(function, items):
    """Apply a function to all items."""
    result = []

    for item in items:
        result.append(function(item))

    return result


def foldl(function, items, initial):
    """Fold a list from the left."""
    result = initial

    for item in items:
        result = function(result, item)

    return result


def foldr(function, items, initial):
    """Fold a list from the right."""
    result = initial

    index = length(items) - 1

    while index >= 0:
        result = function(result, items[index])
        index -= 1

    return result


def reverse(items):
    """Reverse a list."""
    result = []

    index = length(items) - 1

    while index >= 0:
        result.append(items[index])
        index -= 1

    return result