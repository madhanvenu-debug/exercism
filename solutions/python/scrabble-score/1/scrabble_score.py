def score(word):
    values = {
        **dict.fromkeys("AEIOULNRST", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10),
    }

    return sum(values[letter] for letter in word.upper())