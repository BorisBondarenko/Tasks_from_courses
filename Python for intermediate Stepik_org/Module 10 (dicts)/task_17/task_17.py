text_1 = input().lower()
text_2 = input().lower()

for i in ".,!?:;- ":
    text_1 = text_1.replace(i, '')
    text_2 = text_2.replace(i, '')

d_1 = {i: text_1.count(i) for i in text_1}
d_2 = {i: text_2.count(i) for i in text_2}

print("YES" if d_1 == d_2 else "NO")
