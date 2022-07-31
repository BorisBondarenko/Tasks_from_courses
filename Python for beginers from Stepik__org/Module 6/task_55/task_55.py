cities = input(), input(), input()
print(min(cities, key=lambda x: len(x)))
print(max(cities, key=lambda x: len(x)))
