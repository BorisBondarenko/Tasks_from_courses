n = int(input())

myset = set()

for i in range(n):
    city = input()
    if city not in myset:
        myset.add(city)

city = input()
print("OK" if city not in myset else "REPEAT")
