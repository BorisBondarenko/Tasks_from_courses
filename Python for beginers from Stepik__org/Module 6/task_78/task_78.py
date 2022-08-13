nums = input()
res = []
for i in nums.split(' '):
    res.append(int(i))

res.sort()
res_1 = [str(i) for i in res]
print(' '.join(res_1))

res.sort(reverse=True)
res_2 = [str(i) for i in res]
print(' '.join(res_2))
