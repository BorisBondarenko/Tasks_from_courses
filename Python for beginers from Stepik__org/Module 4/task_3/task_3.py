dig = int(input())

_1 = dig // 1000
_2 = (dig // 100) % 10
_3 = (dig // 10) % 10
_4 = dig % 10

if (_1 + _4) == (_2 - _3):
    print('ДА')
else:
    print('НЕТ')