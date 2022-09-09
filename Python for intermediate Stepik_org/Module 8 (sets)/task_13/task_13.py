nums = [int(i) for i in input().split()]

res = set()
for i in nums:
    print("YES" if i in res else "NO")
    res.add(i)
