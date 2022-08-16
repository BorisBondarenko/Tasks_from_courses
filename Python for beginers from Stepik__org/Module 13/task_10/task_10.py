def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]


s = input()
char = input()
print(find_all(s, char))
