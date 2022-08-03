n = int(input())

my_list = [int(input()) for i in range(n)]

for x in my_list:
    print(x)

print()

for y in my_list:
    print((y ** 2) + (2 * y) + 1)
