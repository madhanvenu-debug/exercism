def encode(string):
    if not string:
        return ""

    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result.append(
                (str(count) if count > 1 else "") + string[i - 1]
            )
            count = 1

    result.append(
        (str(count) if count > 1 else "") + string[-1]
    )

    return "".join(result)


def decode(string):
    result = []
    count = ""

    for char in string:
        if char.isdigit():
            count += char
        else:
            result.append(char * (int(count) if count else 1))
            count = ""

    return "".join(result)