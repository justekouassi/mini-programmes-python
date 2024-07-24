E=1
somdue=0
while E!=0 :
        E = int( input("Entrez le montant : "))
        somdue=somdue + E
print ("Vous devez :", somdue, "euros")

M=int(input("Montant versé :"))

reste = M-somdue
nb10e = 0
while reste >= 10 :
        nb10e = nb10e + 1
        reste = reste - 10

nb5e = 0
if reste >= 5:
        nb5e = 1
        reste = reste - 5

print ("Monnaie rendue :")
print ("Billets de 10 euros : ",nb10e)
print ("Billets de 5 euros : ",nb5e)
print ("Pièces de 1 euro : ",reste)
