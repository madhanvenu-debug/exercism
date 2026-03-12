def leap_year(year):
    """Return True if the year is a leap year, otherwise False."""

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False