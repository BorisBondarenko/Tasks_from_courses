student_1 = set(map(int, input().split(' ')))
student_2 = set(map(int, input().split(' ')))
student_3 = set(map(int, input().split(' ')))

scores = set([i for i in range(0, 11)])
all_students = student_1 | student_2 | student_3

print(*sorted(scores.difference(all_students)))
