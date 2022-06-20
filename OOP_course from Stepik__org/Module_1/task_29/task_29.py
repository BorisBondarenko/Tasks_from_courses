from string import ascii_lowercase, digits

class TextInput():
    MIN_LEN = 3
    MAX_LEN = 50

    @classmethod
    def check_name(cls, name):
        if name.isalnum():
            if cls.MIN_LEN <= len(name) <= cls.MAX_LEN:
                return True
        else:
            return False

    def __init__(self, name, size=10):
        self.name = None
        self.size = size

        if self.check_name(name):
            self.name = name
        else:
            raise ValueError('некорректное имя поля')

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput():
    MIN_LEN = 3
    MAX_LEN = 50

    @classmethod
    def check_name(cls, name):
        if name.isalnum():
            if cls.MIN_LEN <= len(name) <= cls.MAX_LEN:
                return True
        else:
            return False

    def __init__(self, name, size=10):
        self.name = None
        self.size = size

        if self.check_name(name):
            self.name = name
        else:
            raise ValueError('некорректное имя поля')

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()