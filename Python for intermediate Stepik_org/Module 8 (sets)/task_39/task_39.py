n = int(input())
m = int(input())

a = []
b = []
for i in range(n + m):
    student = input()
    if student not in a:
        a.append(student)
    else:
        b.append(student)

a = set(a)
b = set(b)
res = a.difference(b)
print(len(res) if res else "NO")
