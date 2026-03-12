"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate seat identifiers like 1A, 1B, 1C... skipping row 13."""
    row = 1
    count = 0
    letters = ["A", "B", "C", "D"]

    while count < number:

        if row == 13:
            row += 1
            continue

        for letter in letters:
            if count >= number:
                break

            yield f"{row}{letter}"
            count += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""
    seat_generator = generate_seats(len(passengers))
    assignments = {}

    for passenger in passengers:
        assignments[passenger] = next(seat_generator)

    return assignments


def generate_codes(seat_numbers, flight_id):
    """Generate 12 character ticket codes."""
    for seat in seat_numbers:
        code = seat + flight_id
        yield code.ljust(12, "0")