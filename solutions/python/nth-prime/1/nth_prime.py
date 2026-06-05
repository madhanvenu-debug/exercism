def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    candidate = 1

    while count < n:
        candidate += 1

        if is_prime(candidate):
            count += 1

    return candidate


def is_prime(num):
    if num < 2:
        return False

    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True