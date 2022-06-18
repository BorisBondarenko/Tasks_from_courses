class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for i in (self.a, self.b, self.c):
            if not isinstance(i, (int, float)):
                return 1
            elif i <= 0:
                return 1
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.c + self.b <= self.a:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
