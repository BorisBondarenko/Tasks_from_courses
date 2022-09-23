n = int(input())

couples = {}
for i in range(n):
    sent = input().split(" ")
    for j in range(1, len(sent)):
        couples[sent[j]] = sent[0]

m = int(input())
for i in range(m):
    question = input()
    print(couples[question])