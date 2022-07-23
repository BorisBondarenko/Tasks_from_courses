import sys


class Player:
    """This class describes the Players instances.
    Also, this class include method __bool__ that allow us define
    the falsity of ours instances."""

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

    def __len__(self):
        return


lst_in = list(map(str.strip, sys.stdin.readlines()))


def form(string):
    name, old, score = list(map(str.strip, string.split(';')))
    return name, int(old), int(score)


players_filtered = list(map(lambda x: Player(*form(x)), lst_in))
players_filtered = list(filter(lambda x: bool(x), players_filtered))
