def make_it_easy(res=''):
    values = input().split()
    try:
        res = sum([int(i) for i in values])
    except ValueError:
        try:
            res = sum([float(i) for i in values])
        except ValueError:
            res = ' '.join(values)
    finally:
        print(res)


make_it_easy()
