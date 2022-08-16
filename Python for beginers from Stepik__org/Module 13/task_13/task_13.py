def is_valid_triangle(a, b, c):
    if a > b and a > c:
        if b + c <= a:
            return False
        else:
            return True

    elif b > a and b > c:
        if a + c <= b:
            return False
        else:
            return True

    elif c > a and c > b:
        if a + b <= c:
            return False
        else:
            return True

    elif a == b == c:
        return True


a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))
