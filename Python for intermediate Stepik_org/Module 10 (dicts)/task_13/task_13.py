phr = input().lower()

for i in ".,!?:;-\t":
    phr = phr.replace(i, '')

dict_ = {i: phr.split(' ').count(i) for i in phr.split(' ')}
res = [k for k, v in dict_.items() if v == min(list(dict_.values()))]

print(min(res))
