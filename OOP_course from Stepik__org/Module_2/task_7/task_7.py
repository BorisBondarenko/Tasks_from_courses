from random import randint, sample

class EmailValidator:

    symbols = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    symbols.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    symbols.extend(list(map(str, range(0, 10))))
    symbols.extend([i for i in ('_', '@', '.')])

    def __new__(cls):
        return None

    def __init__(self, email):
        self.email = email

    @classmethod
    def check_email(cls, email):

        if cls.__is_email_str(email):

            for sym in email:
                if sym in cls.symbols:
                    continue
                else:
                    return False

            if email.count('@') == 1:
                name, domain = email.split('@')

                if '..' in name:
                    return False

                if len(name) > 100:
                    return False

                if len(domain) > 50:
                    return False

                if domain.count('.') == 0 or '..' in domain:
                    return False

                else:
                    return True

            else:
                return False

    @classmethod
    def get_random_email(cls):
        len_name = randint(5, 15)
        name = sample(cls.symbols, len_name)
        return ''.join(map(str, name)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


email = EmailValidator.get_random_email()
print(email)
print(EmailValidator.check_email(email))