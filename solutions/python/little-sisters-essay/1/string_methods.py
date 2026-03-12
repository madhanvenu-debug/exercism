def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase."""
    return title.title()


def check_sentence_ending(sentence):
    """Check if the sentence ends with a period."""
    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """Remove leading and trailing whitespace."""
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace occurrences of old_word with new_word."""
    return sentence.replace(old_word, new_word)
