n = int(input())

res = [input() for i in range(n)]

total = 0
for i in range(n):
    total += int(res[i].split(' ')[i])
print(total)
