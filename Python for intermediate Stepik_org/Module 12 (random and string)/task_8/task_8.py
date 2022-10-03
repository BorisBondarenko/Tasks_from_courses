from random import randint

for i in range(100):
    res = []
    for j in range(7):
        if j == 0:
            res.append(str(randint(1,9)))
        else:
            res.append(str(randint(0,9)))
    print(''.join(res))