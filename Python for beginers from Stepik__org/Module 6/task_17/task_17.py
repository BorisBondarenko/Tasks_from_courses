lst = [input(), input(), input()]
a = min(lst, key=len)
c = max(lst, key=len)

x = (len(a) + len(c)) / 2
print('YES') if x == len(sorted(lst, key=len)[1]) else print('NO')
