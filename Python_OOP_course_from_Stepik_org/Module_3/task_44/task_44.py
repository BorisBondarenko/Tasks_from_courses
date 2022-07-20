import sys


class DataBase:
    """This class describes some database for some users.
    attr: path - path to the file (here it doesn't use);
    attr: dict_db - dict of added objects (key - hash(obj), val - list ot obj with equal hash)
    """

    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):

        if not self.dict_db.get(hash(record), False):
            self.dict_db[hash(record)] = [record]

        elif self.dict_db.get(hash(record), False):
            self.dict_db[hash(record)].append(record)

    def read(self, pk):
        for lists in self.dict_db.values():
            for obj in lists:
                if obj.pk == pk:
                    return obj


class Record:
    """This class describes database records.
    attr: fio - full users name;
    attr: descr - user short-description;
    attr: old - user age;
    attr: pk = uniq id of record (every new Record-instance has self uniq id)."""

    __ID = 0

    def __new__(cls, *args, **kwargs):
        cls.__ID += 1
        return super().__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.__ID

    def __hash__(self):
        return hash((self.fio, self.old))

    def __eq__(self, other):
        if isinstance(other, Record):
            return hash(self) == hash(other)


db = DataBase('path')


def formatting(string):
    """This func prepares data for Record-class."""

    fio, descr, old = list(map(str.strip, string.split(';')))
    return fio, descr, int(old)


lst_in = list(map(str.strip, sys.stdin.readlines()))

for i in lst_in:
    db.write(Record(*formatting(i)))
