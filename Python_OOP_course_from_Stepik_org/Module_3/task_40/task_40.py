class Body:
    """This class describes some chemical-instances in nature.
    attr: name - chemical name;
    attr: ro - material density;
    attr: volume - amount of it what we have (cm3) - for example.

    As result, we can to create some materials and have
    opportunity to compare their wight."""

    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        self_m = self.ro * self.volume
        other_m = other.ro * other.volume if isinstance(other, Body) else other
        return self_m == other_m

    def __lt__(self, other):
        self_m = self.ro * self.volume
        other_m = other.ro * other.volume if isinstance(other, Body) else other
        return self_m < other_m


a = Body('Pb', 8, 1000)
b = Body('Cu', 9, 1000)
print(a > b)
