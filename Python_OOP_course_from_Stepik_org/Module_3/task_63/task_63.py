class Person:
    """This class describes the person with next attrs:
    attr: fio - first and last name of person;
    attr: job - person job;
    attr: old - age of person;
    attr: salary - salary of person;
    attr: year_job - commercial experience on position.

    Main purpose of this mission is the make possible to use it in loops"""

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __len__(self):
        return len(self.__dict__)

    def idx_checker(self, idx):
        if abs(idx) not in range(len(self)):
            raise IndexError('неверный индекс')
        return list(self.__dict__.keys())[idx]

    def __getitem__(self, idx):
        key = self.idx_checker(idx)
        return getattr(self, key)

    def __setitem__(self, idx, value):
        key = self.idx_checker(idx)
        setattr(self, key, value)

    def __iter__(self):
        self.next_idx = -1
        return self

    def __next__(self):
        self.next_idx += 1
        if self.next_idx not in range(len(self) - 1):
            self.__delattr__('next_idx')
            raise StopIteration
        return self[self.next_idx]
