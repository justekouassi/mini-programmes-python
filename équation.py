# Ce programme consiste à résoudre des équations du second degré de la forme ax^2 + bx + c = 0
from math import *

print("Entrez les coefficients de l'équation")
a = int(input("coeff1 = "))
b = int(input("coeff2 = "))
c = int(input("coeff3 = "))

if a == 0:
    if b == 0:
        print("L'équation n'admet pas de solution")
    else:
        print("L'équation admet une solution double", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("L'équation n'admet de solution")
    elif delta == 0:
        print("La solution de l'équation est", -b/2*a)
    else:
        x1 = ((-b-sqrt(delta))/2*a)
        x2 = ((-b+sqrt(delta))/2*a)
        print("L'équation admet deux solutions réelles", x1, "et", x2)
