n = int(input())

# перевод в двоичную систему исч.

b = n
res_b = []
while b != 0:
    res_b.append(b % 2)
    b //= 2
res_b.append(b)

for i in res_b[::-1][1:]:
    print(i, end='')
print()
# перевод в восьмеричную систему исч.

o = n
res_o = []
while o != 0:
    res_o.append(o % 8)
    o //= 8
res_o.append(o)
for i in res_o[::-1][1:]:
    print(i, end='')

print()
# перевод в шестнадцатеричную систему исч.

x = n
values = {d: chr(ord('A') + d - 10) for d in range(10, 15 + 1)}
res_x = []
while x > 0:
    r = x % 16
    if r > 9:
        res_x.append(values[r])
    elif r >= 0:
        res_x.append(r)
    x //= 16
for i in res_x[::-1]:
    print(i, end='')
