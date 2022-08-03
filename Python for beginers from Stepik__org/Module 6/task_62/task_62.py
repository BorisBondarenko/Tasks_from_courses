n = int(input())

my_list = [int(input()) for i in range(n)]
my_list.remove(min(my_list))
my_list.remove(max(my_list))

for i in my_list:
    print(i)
