n = int(input())

tmp = []
for i in range(n):
    a = input()
    tmp.append([int(j) for j in a.split()])

pattern = sum(tmp[0])
answer = True

for i in range(n):
    if sum(tmp[i]) != pattern:
        answer = False
    if 0 in tmp[i]:
        answer = False

for i in range(n):
    total = 0
    x = None
    for j in range(n):
        total += tmp[j][i]
        if tmp[j][i] == x:
            pattern = False
        x = tmp[j][i]
    if total != pattern:
        answer = False

print('YES' if answer else 'NO')