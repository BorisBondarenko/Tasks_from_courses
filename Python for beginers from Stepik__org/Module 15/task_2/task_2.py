phr = input()


def coder(phr, n):
    for i in phr:
        code = ord(i)
        if code not in range(66, 122 + 1):
            print(chr(code), end='')
        elif code == 32:
            print('"', end='')
        elif code in range(66, 92 + 1):
            if code + n <= 92:
                print(chr(code + n), end='')
            else:
                print(chr((code + n - 92) + 66), end='')
        elif code in range(96, 122 + 1):
            if code + n <= 122:
                print(chr(code + n), end='')
            else:
                print(chr((code + n - 122) + 96), end='')
    print(' ', end='')


for word in phr.split(' '):
    counter = 0
    for char in word:
        if char.isalpha():
            counter += 1
    coder(word, counter)
