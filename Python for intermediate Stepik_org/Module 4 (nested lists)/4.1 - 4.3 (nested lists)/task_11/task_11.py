n = input().split()
x = int(input())
print([n[i - x:i] for i in range(x, len(n) + 2, x) if n[i - x:i]])
