ip = input().split('.')

answer = True
for i in ip:
    if 0 > int(i) or int(i) > 255:
        answer = False

print("ДА" if answer else "НЕТ")
