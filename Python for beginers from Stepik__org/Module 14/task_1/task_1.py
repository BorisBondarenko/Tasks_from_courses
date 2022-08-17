def draw_triangle():
    for i in range(1, 15 + 1, 2):
        print(' ' * ((15 - i) // 2) + '*' * i)


draw_triangle()
