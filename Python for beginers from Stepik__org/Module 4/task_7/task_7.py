a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = a if a < b else b
y = c if c < d else d
print(x if x < y else y)
