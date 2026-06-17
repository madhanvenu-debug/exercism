import random
import string

used_names = set()

class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        while True:
            name = (
                ''.join(random.choices(string.ascii_uppercase, k=2))
                + ''.join(random.choices(string.digits, k=3))
            )
            if name not in used_names:
                used_names.add(name)
                self.name = name
                break