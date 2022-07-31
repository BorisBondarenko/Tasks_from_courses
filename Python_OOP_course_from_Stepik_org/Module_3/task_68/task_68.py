from copy import deepcopy


class Matrix:
    """This class describes the Matrix-obj."""

    def __init__(self, rows, cols=0, fill_value=0):
        lst = [[fill_value for _ in range(cols)] for _ in range(rows)] if rows and cols else rows
        self.matrix = self.m_checker(lst)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.sneak_steps = [(j, i) for j in range(cols) for i in range(rows)]

    @staticmethod
    def m_checker(input_m):
        step_1 = len(set(map(len, input_m))) == 1
        step_2 = all(all(map(lambda x: type(x) in (int, float), row)) for row in input_m)
        if not step_1 and step_2:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        return input_m

    def i_checker(self, idx):
        row, coll = idx
        if row > len(self.matrix[0]) - 1 or coll > len(self.matrix[0]) - 1:
            raise IndexError('недопустимые значения индексов')
        return row, coll

    def __getitem__(self, idx):
        row, coll = self.i_checker(idx)
        return self.matrix[row][coll]

    def __setitem__(self, idx, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        row, coll = self.i_checker(idx)
        self.matrix[row][coll] = value

    def __add__(self, matrix_b):
        matrix_a = deepcopy(self.matrix)
        type_ = isinstance(matrix_b, Matrix)
        if type_ and self != matrix_b:
            raise ValueError('операции возможны только с матрицами равных размеров')
        for row, col in self.sneak_steps:
            matrix_a[row][col] += matrix_b.matrix[row][col] if type_ else matrix_b
        return Matrix(matrix_a)

    def __sub__(self, matrix_b):
        matrix_a = deepcopy(self.matrix)
        type_ = isinstance(matrix_b, Matrix)
        if type_ and self != matrix_b:
            raise ValueError('операции возможны только с матрицами равных размеров')
        for row, col in self.sneak_steps:
            matrix_a[row][col] -= matrix_b.matrix[row][col] if type_ else matrix_b
        return Matrix(matrix_a)

    def __eq__(self, other):
        return (self.rows, self.cols) == (other.rows, other.cols)