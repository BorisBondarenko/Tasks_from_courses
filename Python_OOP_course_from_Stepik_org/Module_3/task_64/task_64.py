class TriangleListIterator:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                yield self.lst[i][j]

    def __next__(self):
        return self.lst
