n = int(input())
res = []

for i in range(n):
    res.extend([int(k) for k in input().split(' ')])


def quick_merge():
    res.sort()
    return ' '.join([str(i) for i in res])


print(quick_merge())
