number = input()
a, b, c = int(number[0]), int(number[1]), int(number[2])

print('Число интересное') if max(a, c) - min(a, c) == b or max(a, c) + min(a, c) == b else print('Число неинтересное')
