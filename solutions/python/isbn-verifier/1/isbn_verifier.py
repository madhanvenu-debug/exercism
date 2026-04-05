def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")
    
    # Must be exactly 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    for i in range(10):
        char = isbn[i]

        # Handle 'X' only in last position
        if char == 'X':
            if i != 9:
                return False
            value = 10
        # Handle digits
        elif char.isdigit():
            value = int(char)
        else:
            return False

        # Multiply with decreasing weight (10 → 1)
        total += value * (10 - i)

    # Check validity
    return total % 11 == 0