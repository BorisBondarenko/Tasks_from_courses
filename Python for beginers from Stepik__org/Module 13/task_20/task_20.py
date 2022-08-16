def is_correct_bracket(text):
    counter = 0
    was_negative = False
    if text[0] == '(' and text[-1] == ')':
        for i in text:
            counter += 1 if i == '(' else -1
            if counter < 0:
                was_negative = True
        return True if not counter and not was_negative else False
    else:
        return False


txt = input()
print(is_correct_bracket(txt))
