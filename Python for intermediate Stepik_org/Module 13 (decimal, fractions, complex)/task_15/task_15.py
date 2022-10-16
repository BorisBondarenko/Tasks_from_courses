n = int(input())
z_1 = complex(input())
z_2 = complex(input())

print((z_1 ** n) + (z_2 ** n) + ((z_1.conjugate()) ** (n)) + ((z_2.conjugate()) ** (n + 1)))
