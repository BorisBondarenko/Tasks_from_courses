n = int(input())
m = int(input())

math = {input() for _ in range(n)}
info = {input() for _ in range(m)}
res = len(math.symmetric_difference(info))
print(res if res else "NO")
