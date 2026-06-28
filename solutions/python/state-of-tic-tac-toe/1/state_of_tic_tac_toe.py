def gamestate(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    # Turn order checks
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    def winner(player):
        # Rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # Columns
        for c in range(3):
            if all(board[r][c] == player for r in range(3)):
                return True

        # Diagonals
        if all(board[i][i] == player for i in range(3)):
            return True

        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    x_wins = winner('X')
    o_wins = winner('O')

    # Both players cannot win
    if x_wins and o_wins:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    # X wins only if X has one more move than O
    if x_wins:
        if x_count != o_count + 1:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    # O wins only if both have played equal turns
    if o_wins:
        if x_count != o_count:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    # Board full → draw
    if x_count + o_count == 9:
        return "draw"

    # Otherwise the game is still ongoing
    return "ongoing"