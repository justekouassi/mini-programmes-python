from turtle import *

r = ""
while r == "":
    l = int(input("Longueur de trait : "))

    # Centrage approximatif de la figure
    x = 0-l/2
    y = 0

    e = int(input("Épaisseur de trait : "))
    nc = float(input("Nombre de pointes désirées : "))

    # Correctif de calcul d'angle et de côtés
    na = nc
    if nc % 4 > 0:
        if nc % 2 == 0:
            na = nc/2
        elif nc % 2 > 0:
            na = nc*2
    angle = 360/na
    angle = 180-angle

    reset()
    color("blue")
    c1 = "blue"
    c2 = "red"
    a = 0
    up()
    goto(x, y)
    down()
    width(e)
    while a < nc:
        a += 1
        forward(l)
        left(angle)
        c1, c2 = c2, c1
        color(c1)
    r = input("Tapez [Enter] pour recommencer.")
