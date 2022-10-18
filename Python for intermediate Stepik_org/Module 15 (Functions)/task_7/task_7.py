def info_kwargs(**kwargs):
    res = sorted([(k, v) for k, v in kwargs.items()])
    for k, v in res:
        print(f'{k}: {v}')
