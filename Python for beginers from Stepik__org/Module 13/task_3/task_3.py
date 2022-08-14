fill = input()
base = int(input())


def draw_triangle(fill, base):
    for i in range(((base + 1) // 2) + 1):
        print(fill * i)
    for i in range(((base + 1) // 2) - 1, 0, -1):
        print(fill * i)


draw_triangle(fill, base)
