def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + words)


def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith('i'):
        return root[:-1] + 'y'
    return root


def adjective_to_verb(sentence, index):
    words = sentence.split()
    # Clean punctuation from the target word
    word = words[index].strip('.,!?;:')
    return word + 'en'
