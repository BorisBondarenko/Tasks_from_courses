commands = {'execute': 'X', 'write': 'W', 'read': 'R'}

n = int(input())

files_access = [tuple(input().split(' ')) for i in range(n)]

res = {}
for i in files_access:
    file, *access = i
    res[file] = access

m = int(input())

for i in range(m):
    request = input().split(' ')
    print("OK" if commands[request[0]] in res[request[1]] else "Access denied")
