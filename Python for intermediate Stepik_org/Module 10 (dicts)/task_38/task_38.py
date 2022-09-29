def build_query_string(params):
    res = ''
    for i in sorted(params):
        res += f'{i}={params[i]}&'
    return res[:-1]
