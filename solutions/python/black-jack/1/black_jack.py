def value_of_card(card):
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    
    if val_one > val_two:
        return card_one
    if val_two > val_one:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    # If adding 11 would bust the hand (total > 21) or if an Ace is already present, return 1
    if value_of_card(card_one) + value_of_card(card_two) > 10 or card_one == 'A' or card_two == 'A':
        return 1
    return 11


def is_blackjack(card_one, card_two):
    # A natural blackjack is an Ace and any 10-value card (10, J, Q, K)
    ten_cards = ('10', 'J', 'Q', 'K')
    return (card_one == 'A' and card_two in ten_cards) or \
           (card_two == 'A' and card_one in ten_cards)


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11
