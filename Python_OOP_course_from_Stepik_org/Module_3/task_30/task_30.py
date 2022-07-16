class Lib:
    """This class describes the library as an object that should contain the books-instances.
    To manage the content using usual arithmetic operations (+, -)."""

    def __init__(self):
        self.book_list = []

    @staticmethod
    def type_checker(input_obj):
        if not isinstance(input_obj, Book):
            raise TypeError('I work just with Book-objects')
        return True

    def __add__(self, other):
        self.type_checker(other)
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            self.book_list.pop(other)
        elif isinstance(other, Book):
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)


class Book:
    """That class describes the book-objects."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
