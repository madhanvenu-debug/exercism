def transpose(text):
    rows = text.split('\n')
    max_len = max(len(row) for row in rows)

    result = []

    for col in range(max_len):
        new_row = []

        for row_index, row in enumerate(rows):
            if col < len(row):
                new_row.append(row[col])
            else:
                # Keep spaces only if a later row has a character here
                if any(col < len(r) for r in rows[row_index + 1:]):
                    new_row.append(' ')
                else:
                    break

        result.append(''.join(new_row))

    return '\n'.join(result)