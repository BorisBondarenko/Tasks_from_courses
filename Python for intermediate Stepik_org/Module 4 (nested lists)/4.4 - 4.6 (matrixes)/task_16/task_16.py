n = int(input())

res = [input() for i in range(n)]

for i in res:
    j = [int(j) for j in i.split()]
    mid = sum(j) / len(j)
    j = [k for k in j if k > mid]
    print(len(j))
