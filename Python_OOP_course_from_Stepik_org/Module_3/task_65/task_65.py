class IterColumn:
    """This class describes the iterators which returns needed element of nested list.
    attr: lst - input nested list;
    attr: column - number of element which it must return."""

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]


lst = [['x00', 'x01', 'x02', 'x03'],
       ['x10', 'x11', 'x12', 'x13'],
       ['x20', 'x21', 'x22', 'x23'],
       ['x30', 'x31', 'x32', 'x33']]

obj = IterColumn(lst, 1)

for i in obj:
    print(i)
