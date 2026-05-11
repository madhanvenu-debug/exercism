COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

def resistor_label(colors):

    # One-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # Four-band resistor
    if len(colors) == 4:
        first = COLORS[colors[0]]
        second = COLORS[colors[1]]
        multiplier = COLORS[colors[2]]
        tolerance = TOLERANCE[colors[3]]

        value = (first * 10 + second) * (10 ** multiplier)

    # Five-band resistor
    else:
        first = COLORS[colors[0]]
        second = COLORS[colors[1]]
        third = COLORS[colors[2]]
        multiplier = COLORS[colors[3]]
        tolerance = TOLERANCE[colors[4]]

        value = (first * 100 + second * 10 + third) * (10 ** multiplier)

    # Format value with units
    if value >= 1_000_000_000:
        value = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        value = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value = value / 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    # Remove unnecessary .0
    if isinstance(value, float) and value.is_integer():
        value = int(value)

    return f"{value} {unit} ±{tolerance}"