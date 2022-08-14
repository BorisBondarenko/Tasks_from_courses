n = [int(k) for k in input().split(' ')]
m = [int(r) for r in input().split(' ')]
res = ' '.join([str(n[i] + m[i]) for i in range(len(n))])
print(res)
