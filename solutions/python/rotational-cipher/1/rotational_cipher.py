def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine base (A or a)
            base = ord('A') if char.isupper() else ord('a')
            
            # Shift character
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            # Keep numbers, spaces, punctuation unchanged
            result += char

    return result