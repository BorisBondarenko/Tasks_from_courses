a = int(input())
if a == 9:
    print(int(1107))
else:
    print((a + (a*2)//10)%10, (a*2)%10 + (a*3) // 10, (a*3) % 10, sep='')