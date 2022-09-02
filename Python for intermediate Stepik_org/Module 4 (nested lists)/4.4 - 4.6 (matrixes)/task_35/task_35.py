x, y = input().split()
x = int(x)
y = int(y)

tmp = [str(i) for i in range(1, y + 1)]

for i in range(x):
    print(' '.join(tmp[i % y:] + tmp[:i % y]))
