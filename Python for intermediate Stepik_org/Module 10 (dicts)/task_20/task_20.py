n = int(input())

couples = {}
for i in range(n):
    abonent_ = input().split(" ")
    if not abonent_[1] in couples:
        couples[abonent_[1]] = []
        couples[abonent_[1]].append(abonent_[0])
    else:
        couples[abonent_[1]].append(abonent_[0])

m = int(input())
for i in range(m):
    question = input().capitalize()
    if question in couples:
        print(*couples.get(question))
    else:
        print('абонент не найден')