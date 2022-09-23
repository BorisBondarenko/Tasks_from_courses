n = int(input())

d_1 = {}
d_2 = {}

for i in range(n):
    couple = input().split(' ')
    d_1[couple[0]] = couple[1]
    d_2[couple[1]] = couple[0]

d_1.update(d_2)
print(d_1[input()])
