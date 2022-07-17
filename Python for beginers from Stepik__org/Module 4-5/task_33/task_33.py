x1,y1, x2,y2 = int(input()), int(input()), int(input()), int(input())


if x1 - 2 <= x2 <= x1 + 2 and x2 != x1:
    if y1 - 2 <= y2 <= y1 + 2 and y2 != y1:
        if abs(x1 - x2) != abs(y1 - y2):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')