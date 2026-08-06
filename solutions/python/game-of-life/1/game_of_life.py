def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    next_gen = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += matrix[nr][nc]

            if matrix[r][c] == 1:
                if live_neighbors in (2, 3):
                    next_gen[r][c] = 1
            elif live_neighbors == 3:
                next_gen[r][c] = 1

    return next_gen