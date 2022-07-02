class TVProgram:
    """This class describes TV programs"""

    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        """To add new telecast"""
        if isinstance(tl, Telecast):
            self.items.append(tl)

    def remove_telecast(self, indx):
        """To remove some telecast"""
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


class Telecast:
    """This class describes Telecast"""
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration):
        self.__duration = new_duration
