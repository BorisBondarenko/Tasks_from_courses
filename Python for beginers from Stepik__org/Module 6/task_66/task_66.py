n = int(input())
phr = [input() for i in range(n)]

k = int(input())
search = [input().lower() for j in range(k)]

for j in phr:
    sensor = True
    for i in search:
        if i not in j.lower():
            sensor = False
    if sensor:
        print(j)
