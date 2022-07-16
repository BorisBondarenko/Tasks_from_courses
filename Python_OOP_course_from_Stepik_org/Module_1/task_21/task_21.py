import sys


class ListObject():
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
obj_s = [head_obj]

for i in lst_in[1:]:
    obj_s.append(ListObject(i))

for i in range(0, len(obj_s)):
    if i + 1 == len(obj_s):
        obj_s[i].next_obj = None
    else:
        obj_s[i].next_obj = obj_s[i + 1]
