class Test:
    def __init__(self, descr):
        if len(descr) not in range(10, 10000 + 1):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key == 'ans_digit' and not isinstance(value, (int, float)):
            raise ValueError('недопустимые значения аргументов теста')
        elif key == 'max_error_digit':
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError('недопустимые значения аргументов теста')
        self.__dict__[key] = value

    def run(self):
        ans = float(input())
        min_ = self.ans_digit - self.max_error_digit
        max_ = self.ans_digit + self.max_error_digit
        return True if min_ <= ans <= max_ else False


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)
try:
    test = TestAnsDigit(descr, ans)
    res = test.run()
except Exception as e:
    res = e
finally:
    print(res)
