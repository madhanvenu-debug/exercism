ONES = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]

TEENS = [
    "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

TENS = [
    "", "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
]

SCALES = ["", "thousand", "million", "billion"]


def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    parts = []
    scale = 0

    while number > 0:
        chunk = number % 1000

        if chunk:
            words = _say_chunk(chunk)
            if SCALES[scale]:
                words += f" {SCALES[scale]}"
            parts.append(words)

        number //= 1000
        scale += 1

    return " ".join(reversed(parts))


def _say_chunk(n):
    words = []

    hundreds = n // 100
    remainder = n % 100

    if hundreds:
        words.append(f"{ONES[hundreds]} hundred")

    if remainder:
        if remainder < 10:
            words.append(ONES[remainder])
        elif remainder < 20:
            words.append(TEENS[remainder - 10])
        else:
            tens = remainder // 10
            ones = remainder % 10

            if ones:
                words.append(f"{TENS[tens]}-{ONES[ones]}")
            else:
                words.append(TENS[tens])

    return " ".join(words)