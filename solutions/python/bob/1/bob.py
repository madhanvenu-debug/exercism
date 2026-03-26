def response(hey_bob):
    # Remove leading/trailing whitespace
    msg = hey_bob.strip()

    # Silence
    if msg == "":
        return "Fine. Be that way!"

    # Check if it's a question
    is_question = msg.endswith("?")

    # Check if it's yelling (has letters and all are uppercase)
    is_yelling = msg.isupper()

    # Yelling question
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    # Yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Question
    if is_question:
        return "Sure."

    # Default
    return "Whatever."