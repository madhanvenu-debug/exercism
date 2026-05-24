def translate(text):
    vowels = ("a", "e", "i", "o", "u")

    def pig_latin(word):
        # Rule 1
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        # Rule 3
        if "qu" in word:
            qu_index = word.find("qu")
            if qu_index == 0 or all(c not in vowels for c in word[:qu_index]):
                return word[qu_index + 2:] + word[:qu_index + 2] + "ay"

        # Find first vowel or y
        for i, ch in enumerate(word):
            if ch in vowels or (ch == "y" and i != 0):
                return word[i:] + word[:i] + "ay"

    return " ".join(pig_latin(word) for word in text.split())