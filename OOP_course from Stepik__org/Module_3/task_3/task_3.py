class Course:

    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and isinstance(value, str):
            object.__setattr__(self, key, value)

        elif key == 'practices' and isinstance(value, int):
            object.__setattr__(self, key, value)

        elif key == 'duration' and isinstance(value, int) and value > 0:
            object.__setattr__(self, key, value)

        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.__dict__.keys():
            raise AttributeError("Этот атрибут удалять запрещено.")
        else:
            object.__delattr__(self, item)
