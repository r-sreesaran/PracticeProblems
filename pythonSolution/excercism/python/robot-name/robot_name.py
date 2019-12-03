import random
from string import ascii_uppercase

EXISTING_NAMES = set()


class Robot:

    def __init__(self):
        if len(EXISTING_NAMES) == 676000:
            raise RuntimeError('Name list is full!')

        self.name = self.generate_name()

    def generate_name(self):
        name = "{}{}{}".format(
            random.choice(ascii_uppercase),
            random.choice(ascii_uppercase),
            random.randint(000, 999)
        )
        if name in EXISTING_NAMES:
	    return self.generate_name()
        EXISTING_NAMES.add(name)
        return name

    def reset(self):
        random.seed(0)
        EXISTING_NAMES = set()
        self.name = self.generate_name()