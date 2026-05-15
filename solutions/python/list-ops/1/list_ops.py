def append(list1, list2):
    result = []

    for item in list1:
        result.append(item)

    for item in list2:
        result.append(item)

    return result


def concat(lists):
    result = []

    for lst in lists:
        result = append(result, lst)

    return result


def filter(function, list):
    result = []

    for item in list:
        if function(item):
            result.append(item)

    return result


def length(list):
    count = 0

    for _ in list:
        count += 1

    return count


def map(function, list):
    result = []

    for item in list:
        result.append(function(item))

    return result


def foldl(function, list, initial):
    result = initial

    for item in list:
        result = function(result, item)

    return result


def foldr(function, list, initial):
    result = initial

    index = length(list) - 1

    while index >= 0:
        result = function(result, list[index])
        index -= 1

    return result


def reverse(list):
    result = []

    index = length(list) - 1

    while index >= 0:
        result.append(list[index])
        index -= 1

    return result