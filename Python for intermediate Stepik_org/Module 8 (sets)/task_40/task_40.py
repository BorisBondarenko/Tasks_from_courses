m = int(input())

all_lessons = []
for lessons in range(m):
    students = {input() for lesson in range(int(input()))}
    all_lessons.append(students)

my_set = set()
for i in all_lessons:
    if len(my_set) == 0:
        my_set = set(i)
    else:
        my_set.intersection_update(i)

for res in sorted(my_set):
    print(res)
