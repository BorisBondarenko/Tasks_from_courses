class VideoItem:
    """This class describes video items like objects with parameters.
    attr: title - video title;
    attr: descr - video description;
    attr: path - some path to the video;
    attr: rating - video ranting (it made as rating this is the obj of VideoRating - class)."""

    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value not in range(6) or type(value) != int:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
