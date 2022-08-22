class ValidatorString:
    """This is the class validator, it used for validation Login, Password and other fields.
    attr: rng - range of allowed len of input string;
    attr: chars - string of allowed symbols into input string.

    """

    def __init__(self, min_length, max_length, chars):
        self.rng = range(min_length, max_length + 1)
        self.chars = chars

    def is_valid(self, string):
        type_ = isinstance(string, str)
        lenght_ = len(string) in self.rng
        inter_section_ = set(string) & set(self.chars)

        if self.chars:
            if not type_ or not lenght_ or not inter_section_:
                raise ValueError('недопустимая строка')
        else:
            if not type_ or not lenght_:
                raise ValueError('недопустимая строка')
        return string


class LoginForm:
    """This is the class that describes login-forms for example on web-sites.
    attr: _login - before user insert his login it gets Validator-object;
    attr: _password - before user insert his password it gets Validator-object;"""

    def __init__(self, login_validator, password_validator):
        self._login = login_validator
        self._password = password_validator

    def form(self, request):
        if not request.get('login', False) or not request.get('password', False):
            raise TypeError('в запросе отсутствует логин или пароль')

        inp_log = request.get('login', False)
        inp_pas = request.get('password', False)

        self._login = self._login.is_valid(inp_log)
        self._password = self._password.is_valid(inp_pas)


# For tests:

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")

lg = LoginForm(login_v, password_v)

login, password = input().split()

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
