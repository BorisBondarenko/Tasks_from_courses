import sys


class MailBox:
    """This class describes the MailBox object.
    attr: inbox_list - list of all receved mails;
    meth: receive - to add new mail to list"""

    def __init__(self):
        self.inbox_list = []

    def receive(self, item):
        if isinstance(item, MailItem):
            self.inbox_list.append(item)


class MailItem:
    """This class describes each mail as an object.
    attr: mail_from - sender;
    attr: title - title of mail;
    attr: content - mail content;
    attr: is_read - status flag of mail"""

    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return bool(self.is_read)


def prepare(string):
    mail_from, title, content = list(map(str.strip, string.split(';')))
    return mail_from, title, content


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = map(lambda x: MailItem(*prepare(x)), lst_in)

mail = MailBox()

for i in lst_in:
    mail.receive(i)

mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
