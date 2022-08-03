class Layer:

    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, instance, *args, **kwargs):
        self.next_layer = instance
        return self.next_layer


class Input(Layer):

    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):

    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:

    def __init__(self, first_layer: Layer):
        self.first_layer = first_layer

    def __iter__(self):
        flag = True
        next_one = self.first_layer
        while flag:
            yield next_one
            next_one = next_one.next_layer
            flag = False if next_one is None else True


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)
