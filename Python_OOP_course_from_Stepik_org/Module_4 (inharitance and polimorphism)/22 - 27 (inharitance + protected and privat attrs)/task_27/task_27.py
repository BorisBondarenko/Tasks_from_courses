CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    """This class describes the objects which create class depending on the OS."""

    def __new__(cls, *args, **kwargs):
        title, path, exts = args
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        elif CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(title, path, exts)

    def __init__(self, title, path, exts):
        self.title = title
        self.path = path
        self.exts = exts

    @classmethod
    def create_windows_filedialog(cls, title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @classmethod
    def create_linux_filedialog(cls, title, path, exts):
        return LinuxFileDialog(title, path, exts)

    def some_def(self):
        pass


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
