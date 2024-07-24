p = int(input("Saisir un entier : "))

q = 0
while p>0 :
    i = p%10
    p //= 10
    q *= 10
    q += i

print("Nombre miroir = ",q)
