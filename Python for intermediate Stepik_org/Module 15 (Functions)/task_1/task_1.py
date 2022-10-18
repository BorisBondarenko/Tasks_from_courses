def matrix(n=1, m=None, value=0):
    mat = [[value for j in range(n if m is None else m)] for i in range(n)]
    return mat
