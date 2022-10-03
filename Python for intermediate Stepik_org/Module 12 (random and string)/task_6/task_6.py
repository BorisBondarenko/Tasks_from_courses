from random import sample, choice


def generate_index():
    letters = [chr(i) for i in range(65, 90 + 1)]
    nums = [i for i in range(0, 99 + 1)]
    return f'{"".join(sample(letters, 2))}{choice(nums)}_{choice(nums)}{"".join(sample(letters, 2))}'
