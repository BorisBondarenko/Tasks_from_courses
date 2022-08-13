num = input()
num = [int(i) for i in num.split(' ')]

if len(num) > 1:
    pos_max = num.index(max(num))
    pos_min = num.index(min(num))
    max_ = num.pop(num.index(max(num)))
    min_ = num.pop(num.index(min(num)))
    num.insert(pos_min, max_)
    num.insert(pos_max, min_)
    num = ' '.join([str(i) for i in num])
else:
    num = ''.join([str(i) for i in num])
print(num)
