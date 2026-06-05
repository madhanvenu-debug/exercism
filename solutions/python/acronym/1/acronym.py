import re

def abbreviate(words):
    words = words.replace("-", " ")
    words = re.sub(r"[^A-Za-z\s]", "", words)

    return "".join(word[0].upper() for word in words.split())