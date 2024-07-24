E = 1
somdue = 0
while E != 0:
    E = int(input("Entrez le montant : "))
    somdue = somdue + E
print("Vous devez :", somdue, "euros")

M = int(input("Montant versé :"))

reste = M-somdue
nb10e = 0
while reste >= 10:
    nb10e = nb10e + 1
    reste = reste - 10

nb5e = 0
if reste >= 5:
    nb5e = 1
    reste = reste - 5

print("Monnaie rendue :")
for i in range(1, nb10e+1):
    print("10 euros")
for i in range(1, nb5e+1):
    print("5 euros")
for i in range(1, reste):
    print("1 euro")
