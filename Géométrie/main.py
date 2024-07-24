from math import *

def main(A,B,C):
    xa, xb, xc, ya, yb, yc = A[0], B[0],C[0], A[1], B[1], C[1]
    AB = sqrt((xb-xa)**2+(yb-ya)**2)
    BC = sqrt((xc-xb)**2+(yc-yb)**2)
    AC = sqrt((xc-xa)**2+(yc-ya)**2)
    if AB==BC==AC :
        return "triangle équilatéral"
    elif AB==BC or BC==AC or AB==AC :
        return "triangle isocèle"
    elif AB**2==BC**2+AC**2 or BC**2==AC**2+AC**2 or AC**2==AB**2+BC**2 :
        return "triangle rectangle"
    elif AB**2==2*BC**2 or BC**2==2*AC**2 or AC**2==2*AB**2 :
        return "triangle isocèle rectangle"
    else:
        return "triangle quelconque"
