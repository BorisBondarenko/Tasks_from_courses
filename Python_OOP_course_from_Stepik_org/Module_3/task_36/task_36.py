class StringText:
    """That class describes the objects that transform input string.
    To be more precise - makes strip-operation with these symbols('–?!,.;')."""

    def __init__(self, lst_words):
        lst_words = map(lambda x: x.strip('–?!,.;'), lst_words)
        self.lst_words = list(filter(bool, lst_words))

    def __lt__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        if isinstance(other, StringText):
            return len(self.lst_words) <= len(other.lst_words)

    def __len__(self):
        return len(self.lst_words)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

stich = map(lambda x: x.split(), stich)

lst_text = [StringText(i) for i in stich]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]
