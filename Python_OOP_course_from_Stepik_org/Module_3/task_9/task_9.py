from random import randrange, sample


class RandomPassword:
    """This class describes the model of creating a passwords"""

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        rand_len = randrange(self.min_length, self.max_length + 1)
        return ''.join(sample(self.psw_chars, rand_len))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
r = RandomPassword(psw_chars, min_length, max_length)

lst_pass = (r() for i in range(3))
