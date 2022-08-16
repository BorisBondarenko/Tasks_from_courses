def is_one_away(word1, word2):
    if len(word1) == len(word2):
        res = [i for i in range(len(word1)) if word2[i] != word1[i]]
        return True if len(res) == 1 else False
    else:
        return False


txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))
