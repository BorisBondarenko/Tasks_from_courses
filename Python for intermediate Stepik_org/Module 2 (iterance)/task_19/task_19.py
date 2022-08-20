word = input()
text = f'{word} запретил букву'

for i in range(ord('а'), ord('я') + 1):
    if chr(i) in text:
        print(f'{text} {chr(i)}'.strip().replace(' ' * 3, ' ').replace(' ' * 2, ' '))
        text = text.replace(chr(i), '')
