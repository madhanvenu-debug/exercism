def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)
    diamond = []

    # Top half including middle row
    for i in range(index + 1):
        current = alphabet[i]
        outer_spaces = index - i

        if i == 0:
            row = " " * outer_spaces + "A" + " " * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                " " * outer_spaces
                + current
                + " " * inner_spaces
                + current
                + " " * outer_spaces
            )

        diamond.append(row)

    # Bottom half
    for i in range(index - 1, -1, -1):
        current = alphabet[i]
        outer_spaces = index - i

        if i == 0:
            row = " " * outer_spaces + "A" + " " * outer_spaces
        else:
            inner_spaces = 2 * i - 1
            row = (
                " " * outer_spaces
                + current
                + " " * inner_spaces
                + current
                + " " * outer_spaces
            )

        diamond.append(row)

    return diamond