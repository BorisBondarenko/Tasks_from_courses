n = int(input())
my_list = []
for i in range(n):
    phr = input()
    if phr not in my_list:
        my_list.append(phr)

for j in my_list:
    print(j)
