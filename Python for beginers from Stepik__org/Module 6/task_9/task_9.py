a,b,c = int(input()), int(input()), int(input())

if a == min(a,b,c):
    print(max(b,c))
    print(min(b,c))
    print(a)
elif b == min(a,b,c):
    print(max(a,c))
    print(min(a,c))
    print(b)
elif c == min(a,b,c):
    print(max(a, b))
    print(min(a, b))
    print(c)