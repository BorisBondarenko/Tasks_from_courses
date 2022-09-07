n = input().split()
res = [[]]

for x in range(1, len(n) + 1):
    res.extend([n[i - x:i] for i in range(0, len(n) + 1, 1) if n[i - x:i]])
print(res)
