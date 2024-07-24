# -*-coding:utf-8;-*-
# qpy:3
# qpy:console

while 1:
    n = input("\n\n\n\tveillez entrer le nombre dont vous cherchez l'exposant: ")
    n = int(n)
    i = 2
    q = 0
    c = n  # C pour conserver la valeur de n
    p = input("\n\tveillez entrer l'exposant: ")
    p = int(p)
    if n == 0 and p == 0:
        print("\n\tcalcul erroné!")
    elif n == 0 and p != 0:
        print("\n(", c, ") puissance (", p, ") = 0")
    elif n != 0 and p == 1:
        print("\n(", c, ") puissance (", p, ") = ", n)
    elif n != 0 and p == 0:
        print("l'exposant est 1")
    elif n != 0 and p > 1:
        while i <= p:
            n = c * n
            i += 1
            print("\n(", c, ") puissance (", p, ") = ", n)
    elif n != 0 and p == -1:
        q = 1 / n
        print("\n(", c, ") puissance (", p, ") = ", q)
    elif n != 0 and p < -1:
        while i < -p:
            n = n * c
            q = 1 / n
            i += 1
            print("\n(", c, ") puissance (", p, ") = ", q)
