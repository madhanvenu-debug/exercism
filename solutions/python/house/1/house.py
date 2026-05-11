PARTS = [
    ("house that Jack built.", ""),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def recite(start_verse, end_verse):
    verses = []

    for i in range(start_verse - 1, end_verse):
        verse = f"This is the {PARTS[i][0]}"

        for j in range(i, 0, -1):
            verse += f" that {PARTS[j][1]} the {PARTS[j - 1][0]}"

        verses.append(verse)

    return verses