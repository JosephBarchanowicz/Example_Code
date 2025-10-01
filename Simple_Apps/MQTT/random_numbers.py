# functions that produce the random timers and values

import random


def random_input():
    return random.randint(1, 100)


def random_timer():
    return random.randint(1, 30)


def random_values():
    return [random_input(), random_timer()]