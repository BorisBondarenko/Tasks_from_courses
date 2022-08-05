class SoftList(list):
    """In this class I tried to improve basic list class.
    In case when we try to get some element from list by using wrong index -
    - class will return False instead IndexError"""

    def __getitem__(self, item):
        if item > super().__len__() - 1 or item < -super().__len__():
            return False
        return super().__getitem__(item)


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
