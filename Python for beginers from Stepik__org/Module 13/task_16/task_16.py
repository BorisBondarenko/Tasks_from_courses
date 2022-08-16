def is_password_good(password):
    lenght = False
    is_lower = False
    is_upper = False
    is_num = False
    for i in password:
        if len(password) >= 8:
            lenght = True
        if i.islower():
            is_lower = True
        if i.isupper():
            is_upper = True
        if i.isdigit():
            is_num = True

    return True if lenght and is_upper and is_num and is_lower else False


txt = input()
print(is_password_good(txt))
