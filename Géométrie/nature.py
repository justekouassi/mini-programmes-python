from math import *
from la_distance import *


def equilaterale(A, B, C):
    AB = la_distance(A, B)
    BC = la_distance(B, C)
    AC = la_distance(A, C)
    if AB == BC == AC:
        return "Ce triangle est équilatéral"
    else:
        return "Ce n'est pas un triangle équilatéral"


def isocele(A, B, C):
    AB = la_distance(A, B)
    BC = la_distance(B, C)
    AC = la_distance(A, C)
    if AB == BC or AB == AC or AC == BC:
        return "Ce triangle est isocèle"
    else:
        return "Ce n'est pas un triangle isocèle"


def rectangle(A, B, C):
    AB = la_distance(A, B)
    BC = la_distance(B, C)
    AC = la_distance(A, C)
    if (AB**2 == AC**2+BC**2) or (AC**2 == AB**2+BC**2) or (BC**2 == AB**2+AC**2):
        return "Ce triangle est rectangle"
    else:
        return "Ce n'est pas un triangle rectangle"


def rectangle_isocele(A, B, C):
    AB = la_distance(A, B)
    BC = la_distance(B, C)
    AC = la_distance(A, C)
    if (AB**2 == 2*AC**2) or (AC**2 == 2*AB**2) or (BC**2 == 2*AB**2):
        return "Ce triangle est rectangle isocèle"
    else:
        return "Ce n'est pas un triangle rectangle isocèle"
