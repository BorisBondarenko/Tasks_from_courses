class Translator():
    def add(self, eng, rus):
        if 'base' not in self.__dict__:
            self.base = {}

        if eng in self.base:
            self.base[eng].append(rus)
        else:
            self.base[eng] = [rus]

    def remove(self, eng):
        if eng in self.base:
            del self.base[eng]

    def translate(self, eng):
        return self.base[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))