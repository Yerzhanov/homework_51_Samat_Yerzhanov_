import random
from random import randint


class Cat:
    def __int__(self):
        self.satiety_level = randint(20, 80)
        self.happiness_level = randint(20, 80)
        self.sleep = random.choice([True, False])

    def change_values(self, parameter_name, is_positive=True):
        value = getattr(self, parameter_name)
        if is_positive:
            value += 15
        else:
            value += 5
        if value <= 0:
            raise ValueError
        setattr(self, parameter_name, value)

    def feed(self):
        pass

    def play(self):
        pass

    def go_to_sleep(self):
        pass
