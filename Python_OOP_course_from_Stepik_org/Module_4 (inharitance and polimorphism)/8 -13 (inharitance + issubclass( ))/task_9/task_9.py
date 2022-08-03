class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))



class DictShop(dict):

    def __init__(self, instanse={}):
        if not isinstance(instanse, dict):
            raise TypeError('аргумент должен быть словарем')
        res = {self.__type_checker(k): v for k, v in instanse.items()}
        super().__init__(res)

    @staticmethod
    def __type_checker(value):
        if not isinstance(value, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return value

    def __setitem__(self, key, value):
        self.__type_checker(key)
        super().__setitem__(key, value)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
print(dict_things)
dict_things[th_1] = th_1
dict_things[th_2] = th_2
print(dict_things)

for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError
