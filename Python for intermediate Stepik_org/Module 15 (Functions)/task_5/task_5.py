def greet(name, *args):
    res = f'Hello, {name}'
    for i in args:
        res += f' and {i}'
    return res + '!'
