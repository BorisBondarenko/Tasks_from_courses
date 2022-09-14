n = int(input())
m = int(input())

math = {input() for _ in range(n)}
info = {input() for _ in range(m)}

print(len(math.difference(info)))
