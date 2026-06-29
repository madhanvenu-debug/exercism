def saddle_points(matrix):
    if not matrix:
        return []

    row_length = len(matrix[0])

    # Check for irregular matrix
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    result = []

    for i, row in enumerate(matrix):
        row_max = max(row)

        for j, value in enumerate(row):
            column = [matrix[r][j] for r in range(len(matrix))]
            col_min = min(column)

            if value == row_max and value == col_min:
                result.append({"row": i + 1, "column": j + 1})

    return result