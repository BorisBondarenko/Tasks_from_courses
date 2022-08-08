class Aircraft:
    """This class describes aircraft in general.
    With attrs: model, mass, speed, top.
    And also this class using as basic class for other more specific classes as:
    - PassengerAircraft
    - WarPlane
    For specification of this child-classes I had to overwrite __init__ magic methods."""

    def __init__(self, model, mass, speed, top):
        self._model = model if type(model) == str else self._err()
        self._mass = self._pos(mass) if type(mass) in (int, float) else self._err()
        self._speed = self._pos(speed) if type(speed) in (int, float) else self._err()
        self._top = self._pos(top) if type(top) in (int, float) else self._err()

    def _err(self):
        raise TypeError('неверный тип аргумента')

    def _pos(self, value):
        if value <= 0:
            raise TypeError('неверный тип аргумента')
        return value


class PassengerAircraft(Aircraft):
    """Child class of Aircraft"""

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self._pos(chairs) if type(chairs) == int else self._err()


class WarPlane(Aircraft):
    """Child class of Aircraft"""

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons if type(weapons) == dict else self._err()


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
