n = input()
x = len(n) // 3
res = list(n)

for i in range(-3, -120, -4):
    if x >= 1:
        res.insert(i, ',')
        x -= 1
    else:
        continue
print(''.join(res) if res[0].isdigit() else ''.join(res[1:]))
