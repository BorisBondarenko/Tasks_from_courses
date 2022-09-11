all_scores = [set(map(int, input().split(' '))) for j in range(3)]
res = [all_scores[-1].difference_update(i) for i in all_scores[:-1]]

print(*sorted(all_scores[-1], reverse=True))
