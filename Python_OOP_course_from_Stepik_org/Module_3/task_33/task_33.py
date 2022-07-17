import numpy as np


class MaxPooling:
    """This class describes the objects that separate matrix for equal sectors,
    and then saves max value from each sector.

    size: (horizontal, vertical) - sizes of sector that shifts inside input matrix;
    step: (horizontal, vertical) - steps for sector shifting inside input matrix"""

    def __init__(self, step: tuple, size: tuple):
        self.step = (2, 2) if not step else step
        self.size = (2, 2) if not size else size

    @staticmethod
    def check_matrix(matrix):
        """This method makes checking for input matrix.
        1. Checking for values type inside. It should be INT or FLOAT.
        2. Checking for equality of rows length inside matrix."""

        checking_result = all(map(lambda x: len(x) == len(matrix[0]), matrix))
        if not checking_result:
            raise ValueError("Wrong matrix format!")

        for i in matrix:
            input_len = len(i)
            output_len = len(list(filter(lambda x: type(x) in (int, float), i)))

            if input_len != output_len:
                raise ValueError("Wrong matrix format!")

        return True

    def __call__(self, matrix, *args, **kwargs):

        self.check_matrix(matrix)
        g_size = self.size[0]
        v_size = self.size[-1]

        result = []
        for v_step in list(range(0, len(matrix), self.step[-1])):  # vertical shifting (steps)
            for g_step in list(range(0, len(matrix[0]), self.step[0])):  # horizontal shifting (steps)
                tmp = []
                for i in matrix[v_size - v_size + v_step: v_size + v_step]:
                    tmp += (j for j in i[g_size - g_size + g_step: g_size + g_step])
                if len(tmp) == v_size * g_size:
                    result.append(max(tmp))

        sp_tmp = map(list, np.array_split(result, v_size))
        return list(filter(lambda x: x if x else '', sp_tmp))
