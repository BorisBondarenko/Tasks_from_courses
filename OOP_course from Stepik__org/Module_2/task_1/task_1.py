class Clock:

    def __init__(self, time=0):
        self.__time = time

    def __check_time(self, tm):
        return True if isinstance(tm, int) and 0 <= tm < 100_000 else False

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

clock = Clock(4530)
