def is_palindrome(text):
    text = text.lower()
    for i in (' ', '-', '.', ',', ' ', '!', '?'):
        text = text.replace(i, '')
    return True if text == text[::-1] else False


txt = input()
print(is_palindrome(txt))
