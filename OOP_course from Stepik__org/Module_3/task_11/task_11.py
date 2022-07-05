from string import ascii_lowercase, digits


class LoginForm:
    """This class describes Login-form"""

    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    """This class describes the objects for validation the strings by using the length"""

    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, string, *args, **kwargs):
        return self.min_len <= len(string) <= self.max_len


class CharsValidator:
    """This class describes the objects for validation the strings by using the chars"""

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string, *args, **kwargs):

        for i in string:
            if i not in self.chars:
                return False
        else:
            return True


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")