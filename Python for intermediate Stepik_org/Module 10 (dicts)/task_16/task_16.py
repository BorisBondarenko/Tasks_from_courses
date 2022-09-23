phr_1 = input()
d_1 = {i: phr_1.count(i) for i in phr_1}
phr_2 = input()
d_2 = {i: phr_2.count(i) for i in phr_2}

print("YES" if d_1 == d_2 else "NO")
