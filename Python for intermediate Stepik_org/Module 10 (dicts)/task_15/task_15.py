n = int(input())

definitions = {}
for i in range(n):
    phr = input().split(':')
    definitions[phr[0].lower()] = phr[1].strip()

m = int(input())

for i in range(m):
    word = input().lower()
    print(definitions.get(word, 'Не найдено'))
