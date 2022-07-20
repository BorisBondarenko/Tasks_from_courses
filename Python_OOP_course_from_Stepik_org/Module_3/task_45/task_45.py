import sys


class BookStudy:
    """This class describes the books as an objects."""

    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))


def form(string):
    """I use this func to prepare data for creating BookStudy object."""
    fio, descr, old = list(map(str.strip, string.split(';')))
    return fio, descr, int(old)


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = list(map(lambda x: BookStudy(*form(x)), lst_in))

unique_books = len(set([hash(i) for i in lst_bs]))
