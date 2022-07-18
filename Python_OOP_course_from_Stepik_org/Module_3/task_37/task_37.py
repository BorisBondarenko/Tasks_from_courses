class Morph:
    """This class describes the objects that collect sets of morphological simular words.
    And then each instance using to compare equality with others words in the texts."""

    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.words

#  5 sets of morphologically similar words
dict_words = [['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'],
              ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'],
              ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами',
               'векторах'],
              ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами',
               'эффектах'],
              ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']]

#  Here we create the list of Morph-objects from our set
dict_words = list(map(lambda x: Morph(*x), dict_words))

#  input() string should be split and should be cleared from chars
text = list(map(lambda x: x.strip('.,!?-'), input().split()))

#  Here we count the amount of matches from input() in our dict_words (Morph-objs)
print(sum([1 for i in text for j in dict_words if i == j]))
