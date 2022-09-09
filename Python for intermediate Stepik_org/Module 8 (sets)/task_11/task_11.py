n = int(input())

phr = ''
for i in range(n):
    phr += input().lower()

print(len(set(phr)))
