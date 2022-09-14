set_1 = {int(i) for i in input().split(" ")}
set_2 = {int(i) for i in input().split(" ")}

res = sorted(set_1 & set_2, reverse=True)
print('BAD DAY') if len(set_1 & set_2) == 0 else print(*res)
