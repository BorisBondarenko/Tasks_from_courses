class StringDigit(str):

    @staticmethod
    def check_str(string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return string

    def __init__(self, string):
        super().__init__()
        self.string = self.check_str(string)

    def __add__(self, other):
        other = self.check_str(other)
        return StringDigit(self.string + other)

    def __radd__(self, other):
        other = self.check_str(other)
        return StringDigit(other + self.string)


sd = StringDigit("123")
sd = sd + "456"  # StringDigit: 123456
print(sd)
sd = "789" + sd  # StringDigit: 789123456
print(sd)
# sd = sd + "12f"  # ValueError
print(sd)
