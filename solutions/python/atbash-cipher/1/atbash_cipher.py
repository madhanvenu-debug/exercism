def transform(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]

    if char.isalpha():
        index = alphabet.index(char.lower())
        return reversed_alphabet[index]
    return char


def encode(plain_text):
    cleaned = ""

    for char in plain_text:
        if char.isalnum():
            cleaned += transform(char)

    groups = [cleaned[i:i + 5] for i in range(0, len(cleaned), 5)]
    return " ".join(groups)


def decode(ciphered_text):
    decoded = ""

    for char in ciphered_text:
        if char != " ":
            decoded += transform(char)

    return decoded