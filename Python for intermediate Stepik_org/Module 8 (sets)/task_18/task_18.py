num_1 = input()
num_2 = input()

print("NO" if set(num_1).isdisjoint(list(num_2)) else "YES")
