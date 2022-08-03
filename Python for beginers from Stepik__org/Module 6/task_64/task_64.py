n = int(input())
my_list = [input() for i in range(n)]

search = input().lower()

for j in my_list:
    if search in j.lower():
        print(j)
