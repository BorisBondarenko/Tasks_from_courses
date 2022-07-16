class Recipe:
    """This class describes the recipe-objects that collect the ingredients for dish"""

    def __init__(self, *args):
        self.ing_ts = list(args)

    def add_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ing_ts.append(ing)

    def remove_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ing_ts.remove(ing)

    def get_ingredients(self):
        return tuple(self.ing_ts)

    def __len__(self):
        return len(self.ing_ts)


class Ingredient:
    """This class describes the ingredient in itself for future dish"""

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'
