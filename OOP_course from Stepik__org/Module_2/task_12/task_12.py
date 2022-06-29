class TreeObj:

    def __init__(self, idx, value=None):
        self.idx = idx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_left):
        self.__left = new_left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_right):
        self.__right = new_right


class DecisionTree:
    all_obj_s = []

    @classmethod
    def predict(cls, root, x):
        obj = root.left if x[0] else root.right
        idx = cls.all_obj_s.index(obj)
        return obj.left.value if x[idx] else obj.right.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):

        if isinstance(obj, TreeObj):
            cls.all_obj_s.append(obj)
            if node and left:
                node.left = obj
            elif node and not left:
                node.right = obj
        return obj
