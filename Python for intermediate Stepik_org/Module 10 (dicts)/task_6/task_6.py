d = {"1": ".,?!:",
     "2": "ABC",
     "3": "DEF",
     "4": "GHI",
     "5": "JKL",
     "6": "MNO",
     "7": "PQRS",
     "8": "TUV",
     "9": "WXYZ",
     "0": " "}

phr = input().upper()

for i in phr:
    for key, val in d.items():
        if i in val:
            print(f'{key * (val.index(i) + 1)}', end='')
