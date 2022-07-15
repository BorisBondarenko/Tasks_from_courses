a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())


if a2 > b1 or b2<a1:
    print('пустое множество')
elif a2 == b1:
    print(a2)
elif a2 < b1:
    if a2 > a1 and b2 > b1:
        print(a2, b1)
    elif a2 <= a1 and b2 > b1:
        print(a1, b1)
    elif a2 == a1 and b2 < b1:
        print(a1, b2)
    elif a2 > a1 and b2 == b1:
        print(a2, b2)
    elif a2 > a1 and b2 < b1:
        print(a2, b2)
    elif a2 < a1:
        if b2 == b1 and b2 != a1:
            print(a1, b1)
        elif a1 < b2 < b1:
            print(a1, b2)
        elif b2 == a1:
            print(b2)