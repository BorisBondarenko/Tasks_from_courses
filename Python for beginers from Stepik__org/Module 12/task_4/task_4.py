num = [i for i in input().split('-')]

detector = True
r = [0, 1, 2] if len(num) == 4 else [0, 1]

for i in num:
    if not i.isdigit():
        detector = False

for i in range(1, len(num) - 1):
    if detector and int(num[i]) > 999:
        detector = False

if detector and len(num) == 4 and int(num[0]) != 7:
    detector = False

if detector and int(num[-1]) > 9999:
    detector = False

print('YES' if detector else 'NO')
