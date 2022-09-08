phr = input().split()
set_1 = set()

res = []
for i in phr:
    res.append(True if set(i) == set_1 else False)
    set_1 = set(i)

print("YES" if False not in set(res[1:]) else "NO")
