from abc import ABC, abstractmethod


class CountryInterface(ABC):
    """This is the basic-class for class Country.
    This class supply the interface for class Country instances."""

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    """Mian class here. He's describes country as an objects with attrs:
    attr: _name - country name;
    attr: _population - total population;
    attr: _square - total square."""

    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f'{self._name}: {self._square}, {self._population}'