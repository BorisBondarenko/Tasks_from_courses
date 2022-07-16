class SingletonFive():
    __obj_counter = 5
    __last_obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj_counter:
            cls.__last_obj = super().__new__(cls)
            cls.__obj_counter -= 1
        return cls.__last_obj

    def __del__(self):
        if SingletonFive.__obj_counter < 5:
            SingletonFive.__obj_counter += 1

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]