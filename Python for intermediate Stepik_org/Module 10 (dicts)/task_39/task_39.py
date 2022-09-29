def merge(values):
    keys_ = []
    for i in values:
        for j in i.keys():
            keys_.append(j)

    res = {}
    for i in values:
        for j in keys_:
            if j in i:
                if j not in res:
                    res[j] = set()
                    res[j].add(i[j])
                else:
                    res[j].add(i[j])
            else:
                continue
    return res
