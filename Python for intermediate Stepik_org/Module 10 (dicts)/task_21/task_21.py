shifr = input()

n = int(input())

letters = {}

for i in range(n):
    couple = input().split(": ")
    letters[int(couple[1])] = couple[0]

for i in shifr:
    print(letters[shifr.count(i)], end='')
