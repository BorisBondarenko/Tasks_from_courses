class Book:
    """This class describes boors as an objects.
    This is also a parent-class for DigitBook class, that have additional attrs."""

    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    """This class describes Ebooks, and is the child-class from Books-class"""

    def __init__(self, title, author, pages, year, size: int, frm: str):
        super().__init__(title, author, pages, year)
        self.size = size
        self.year = year
        self.frm = frm
