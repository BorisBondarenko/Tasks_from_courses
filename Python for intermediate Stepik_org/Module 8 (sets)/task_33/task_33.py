m = int(input())
n = int(input())

my_books = {input() for i in range(m)}
for_summer = [input() for i in range(n)]

for book in for_summer:
    print("YES" if book in my_books else "NO")
