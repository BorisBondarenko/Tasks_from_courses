n = int(input())
m = int(input())

tmp = [[int(j) for j in input().split(' ')] for i in range(n)]

chg = [int(i) for i in input().split(' ')]

for i in range(n):
    for j in range(1):
        tmp[i][min(chg)], tmp[i][max(chg)] = tmp[i][max(chg)], tmp[i][min(chg)]

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()
