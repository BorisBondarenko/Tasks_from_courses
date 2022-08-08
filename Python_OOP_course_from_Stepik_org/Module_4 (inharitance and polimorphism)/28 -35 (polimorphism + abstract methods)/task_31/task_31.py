from abc import ABC, abstractmethod


class Model(ABC):
    """This is the basic - class for other some-model classes.
    Here we have meth: get_pk (abstractmethod) that should be redefined in the child-classes."""

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    INSTANCE_ID = 0

    def __new__(cls, *args, **kwargs):
        cls.INSTANCE_ID += 1
        return object.__new__(cls)

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.INSTANCE_ID

    def get_pk(self):
        return self._id

