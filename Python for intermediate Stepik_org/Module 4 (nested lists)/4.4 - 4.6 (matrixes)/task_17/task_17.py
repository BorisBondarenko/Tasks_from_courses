res = [input().split(' ') for i in range(int(input()))]
print(max([max([int(res[i][j]) for j in range(i + 1)]) for i in range(len(res))]))
