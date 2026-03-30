def is_isogram(string):
    cleaned = string.lower()
    seen = set()

    for char in cleaned:
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)

    return True