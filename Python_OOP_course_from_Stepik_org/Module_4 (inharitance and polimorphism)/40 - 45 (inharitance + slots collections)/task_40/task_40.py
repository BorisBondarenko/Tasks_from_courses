class Person:
    """This class describes person as an object.
    The instances of this class have the opportunity to have just 3 attrs: _fio, _old, _job.
    I made this by using __slots__ collection."""
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


p_1 = Person('Суворов', 52, 'полководец')
p_2 = Person('Рахманинов', 50, 'пианист, композитор')
p_3 = Person('Балакирев', 34, 'программист и преподаватель')
p_4 = Person('Пушкин', 32, 'поэт и писатель')

persons = [p_1, p_2, p_3, p_4]
