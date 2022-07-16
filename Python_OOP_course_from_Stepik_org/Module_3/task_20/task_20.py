class WordString:
    """This class describes the objects that count the words in the sentence"""

    def __init__(self, string=''):
        self.string = string
        self.lst_string = []

    @classmethod
    def writer(cls, raw_str):
        """this funk make basic work.
        It used in the setter bellow"""
        return raw_str, list(map(str.strip, raw_str.split()))

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, new_str):
        self.__string = self.writer(new_str)[0]
        self.__lst_string = self.writer(new_str)[-1]

    def __len__(self):
        return len(self.__lst_string)

    def __call__(self, idx, *args, **kwargs):
        return self.__lst_string[idx]


words = WordString()
words.string = "Hello everyone! I tell it in 2022"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Amount of words: {n}; First word: {first}")
