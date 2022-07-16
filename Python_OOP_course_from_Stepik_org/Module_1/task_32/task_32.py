class Application():

    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore():

    __APPS = []

    def add_application(self, app):
        self.__APPS.append(app)

    def remove_application(self, app):
        self.__APPS.remove(app)

    def block_application(self, app):
        idx = self.__APPS.index(app)
        self.__APPS[idx].blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.__APPS)
