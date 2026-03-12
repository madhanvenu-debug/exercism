def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Check if an approximate average equals the true average."""
    true_average = card_average(hand)

    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return first_last_avg == true_average or middle_card == true_average


def average_even_is_average_odd(hand):
    """Check if the average of even-indexed cards equals odd-indexed cards."""
    even_cards = hand[0::2]
    odd_cards = hand[1::2]

    even_avg = sum(even_cards) / len(even_cards)
    odd_avg = sum(odd_cards) / len(odd_cards)

    return even_avg == odd_avg


def maybe_double_last(hand):
    """Multiply the last card by 2 if it is a Jack (value 11)."""
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
