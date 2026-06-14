class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = self.card_num.replace(" ", "")

        # Must contain only digits
        if not num.isdigit():
            return False

        # Must be more than one digit
        if len(num) <= 1:
            return False

        total = 0
        reverse_digits = num[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)

            if i % 2 == 1:  # Every second digit from the right
                n *= 2
                if n > 9:
                    n -= 9

            total += n

        return total % 10 == 0