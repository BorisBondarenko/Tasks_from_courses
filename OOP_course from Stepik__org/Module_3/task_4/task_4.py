class Museum:
    """This class describes the museums in general"""

    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        """To append new art-item"""
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        """To remove new art-item"""
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        """To get the info about each needed item"""
        obj = self.exhibits[indx]
        return f"Описание экспоната {obj.name}: {obj.descr}"


class Picture:
    """This class describes the Picture as an art-item"""

    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    """This class describes the Mummies as an art-item"""

    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    """This class describes the Papyruse as an art-item"""

    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr
