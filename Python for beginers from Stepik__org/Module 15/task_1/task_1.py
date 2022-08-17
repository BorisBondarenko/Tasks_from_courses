def find_double_log(n):
    for j in range(1, 23):
        res = (i for i in range(1, (2 ** j) + 1))
        if n in res:
            return j


print(find_double_log(int(input())))
