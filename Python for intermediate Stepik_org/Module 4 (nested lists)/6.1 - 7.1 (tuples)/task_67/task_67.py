n = int(input())

all_stutents = [input().split() for i in range(n)]
for i in all_stutents:
    print(' '.join(i))

print()

good_students = [i for i in all_stutents if int(i[-1]) > 3]
for i in good_students:
    print(' '.join(i))
