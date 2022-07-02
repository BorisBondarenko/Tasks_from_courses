class StringValue:
    """This descriptor getting in input validation-func"""
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class ValidateString:
    """This class describe all validations-rules and then using in Descriptor"""
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        """Validation rules"""
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class RegisterForm:
    """This class created to get customer-form"""
    login = StringValue(validator=ValidateString(3, 100))
    password = StringValue(validator=ValidateString(3, 100))
    email = StringValue(validator=ValidateString(3, 100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        """Return customer-form in list"""
        return [self.login, self.password, self.email]

    def show(self):
        """Print customer-form in console"""
        print(f"<form>\nLogin: <{self.login}>\nPassword: <{self.password}>\nEmail: <{self.email}>\n</form>""")
