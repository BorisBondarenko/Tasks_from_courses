n = int(input())

tmp = [input().split(' ') for i in range(n)][::-1]

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()
