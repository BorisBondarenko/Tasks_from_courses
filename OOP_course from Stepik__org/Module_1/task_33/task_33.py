class Message():

    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber():
    __MESSAGES = []

    @classmethod
    def add_message(cls, msg):
        cls.__MESSAGES.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.__MESSAGES.remove(msg)

    @classmethod
    def set_like(cls, msg):
        idx = cls.__MESSAGES.index(msg)
        cls.__MESSAGES[idx].fl_like = False if cls.__MESSAGES[idx].fl_like else True

    @classmethod
    def show_last_message(cls, num):
        print(cls.__MESSAGES[-num].text)

    @classmethod
    def total_messages(cls):
        return len(cls.__MESSAGES)
