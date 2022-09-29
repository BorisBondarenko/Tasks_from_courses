d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

counter = 0
for i in input():
    for j in d:
        if i in d[j]:
            counter += j

print(counter)
