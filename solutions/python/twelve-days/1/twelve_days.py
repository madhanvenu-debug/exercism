def recite(start_verse, end_verse):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming",
    ]

    verses = []

    for verse_num in range(start_verse, end_verse + 1):
        verse = (
            f"On the {days[verse_num - 1]} day of Christmas "
            f"my true love gave to me: "
        )

        parts = []

        for i in range(verse_num, 0, -1):
            if i == 1 and verse_num > 1:
                parts.append("and " + gifts[0])
            else:
                parts.append(gifts[i - 1])

        verse += ", ".join(parts)
        verses.append(verse)

    return verses