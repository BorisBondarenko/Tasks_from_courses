phr = input()

counter = 0
res = []
for i in phr:
    if i == 'Р':
        counter += 1
    elif i == 'О':
        res.append(counter)
        counter = 0
res.append(counter)

print(max(res))
