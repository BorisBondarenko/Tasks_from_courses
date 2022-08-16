def convert_to_python_case(text):
    text = text + '_'
    res = ''
    for i in range(len(text) - 1):
        if text[i].isupper() or text[i].islower():
            res += text[i].lower()
        if text[i + 1].isupper():
            res += '_'
        if text[i].isdigit():
            res += text[i]
        if text[i] == '_':
            break
    return res


txt = input()
print(convert_to_python_case(txt))
