import random


def generate_ip():
    string_ = ''
    for i in range(4):
        string_ += f'{random.randint(0, 255)}.'
    return string_[:-1]
