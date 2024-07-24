print("Ce programme vise à déterminer le plus petit entier n tel que la somme des inverses de 1 à n soit supérieure à un certain nombre donné")

E = int(input("Donner un entier naturel : "))
somme_inv = 0
k = 0
while somme_inv < E:
    k += 1
    somme_inv += 1/k
print("Le plus petit entier n recherché est", k)
