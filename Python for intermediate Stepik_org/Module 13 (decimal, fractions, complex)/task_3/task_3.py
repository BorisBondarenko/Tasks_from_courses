from decimal import *

num = Decimal(input())
tuple_num = num.as_tuple()

print(sum([max(tuple_num.digits), min(tuple_num.digits) if abs(num) > 1 else 0]))
