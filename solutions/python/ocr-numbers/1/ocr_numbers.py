def convert(input_grid):
    # Validate row count
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Validate column count
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    digits = {
        (" _ ",
         "| |",
         "|_|",
         "   "): "0",

        ("   ",
         "  |",
         "  |",
         "   "): "1",

        (" _ ",
         " _|",
         "|_ ",
         "   "): "2",

        (" _ ",
         " _|",
         " _|",
         "   "): "3",

        ("   ",
         "|_|",
         "  |",
         "   "): "4",

        (" _ ",
         "|_ ",
         " _|",
         "   "): "5",

        (" _ ",
         "|_ ",
         "|_|",
         "   "): "6",

        (" _ ",
         "  |",
         "  |",
         "   "): "7",

        (" _ ",
         "|_|",
         "|_|",
         "   "): "8",

        (" _ ",
         "|_|",
         " _|",
         "   "): "9",
    }

    result = []

    # Process each 4-line block
    for block_start in range(0, len(input_grid), 4):
        rows = input_grid[block_start:block_start + 4]
        line = []

        for col in range(0, len(rows[0]), 3):
            cell = tuple(row[col:col + 3] for row in rows)
            line.append(digits.get(cell, "?"))

        result.append("".join(line))

    return ",".join(result)