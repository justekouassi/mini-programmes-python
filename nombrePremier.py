# -*-coding:utf-8;-*-
# qpy:3
# qpy:console

while 2:
    print("--------DETERMINATION DE NOMBRE PREMIER--------")
    n = input("\nEntrez un nombre : ")
    n = int(n)
    d = 2
    if n == 0:
        print("\n\n\t0 n'est pas premier! 👎😒\n\n")
    elif 2 <= n <= 3:
        print(" \n\n\t", n, "est premier!👏👏👍\n\n")
    elif n == 1:
        print("1 n'est pas premier! 👎😒\n\n")
    elif 3 < n:
        while d <= n-1:
            r = n % d
            d += 1
            if r == 0:
                print(n, " n'est pas premier! 👎😒\n\n")
                break
            elif d == n-1 and r != 0:
                print(n, " est premier ! 👏👏👍\n\n")
