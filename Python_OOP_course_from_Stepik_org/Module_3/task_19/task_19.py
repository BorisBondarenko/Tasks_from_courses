class Model:

    def query(self, **kwargs):
        for key, val in kwargs.items():
            self.__setattr__(key, val)

    def __str__(self):

        if len(self.__dict__) != 0:
            res = 'Model: '
            for k, v in self.__dict__.items():
                res += f'{k} = {v},'
            return res[:-1]

        else:
            return 'Model'


model = Model()
model.query(name='Boris', surname='Bond', age=29)
print(model)
