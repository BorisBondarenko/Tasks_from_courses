class WindowDlg:

    MIN = 0
    MAX = 10000

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if isinstance(new_width, int):
            if self.MIN <= new_width <= self.MAX:
                self.__width = new_width
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if isinstance(new_height, int):
            if self.MIN <= new_height <= self.MAX:
                self.__height = new_height
                self.show()