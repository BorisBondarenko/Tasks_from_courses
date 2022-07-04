class SmartPhone:
    """This class describes smartphone as a container for apps"""

    def __init__(self, model):
        self.model = model
        self.apps = []

    def check_presence(self, obj):
        answer = list(filter(lambda x: type(x) == obj.__class__, self.apps))
        return True if not answer else False

    def add_app(self, app):
        if self.check_presence(app):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    """This simple class describes app Vkontakte"""

    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:
    """This simple class describes app YouTube"""

    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    """This simple class describes default Phone-app in the smartphone"""

    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list
