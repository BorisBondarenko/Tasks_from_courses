TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog():

    __instance = None

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            cls.__instance = super().__new__(DialogWindows)
        else:
            cls.__instance = super().__new__(DialogLinux)

        cls.__instance.name = args[0]
        return cls.__instance

    def __init__(self, name):
        self.name = name


dig = Dialog('первый')
print(dig.name)