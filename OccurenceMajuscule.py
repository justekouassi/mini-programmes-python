#Donner le nombre de lettres majuscules contenues dans une phrase

def Chaineliste(phrase) :
    liste = []
    i,y = 0, 0

    while i < len(phrase) :

        if (phrase[i] == ' ' or phrase[i] == "'") or i == len(phrase)-1:

            if i == len(phrase)-1 :
                i += 1

            if len(phrase[y:i]) == 1 :
                liste.append(phrase[y:i+1])
            else :
                liste.append(phrase[y:i])

            i += 1
            y = i

        else :
            i += 1

    return liste
    
def estUneMaj(argument) :
    liste_majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if argument in liste_majuscules :
        return True
    else :
        return False

phrase = input("Entrer la phrase : ")

liste = Chaineliste(phrase)
compteur = 0

for i in range(len(phrase)) :
    for j in range(len(phrase[i])) :
        if estUneMaj(phrase[i][j]) == True :
            compteur += 1
print("Il y a ",compteur,"lettre(s) majuscule(s) dans la phrase :\n ",phrase)
