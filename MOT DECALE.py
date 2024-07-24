# k : représente le nombre de décalages à effectuer
# pour k positif, on a un décalage à droite

def normal(x, k):
    return (x+k) % 26


def anormal(x, k):
    return (x-k) % 26


def decale(mot, k):
    msg = ''
    for lettre in mot:
        nb = ord(lettre)-65
        nbcrypt = normal(nb, k+20)
        lettrecrypt = chr(nbcrypt+65)
        msg += lettrecrypt
    return msg


mot = input("Entrer le mot à décalé : ").lower()
decalage = int(input("On décale à combien de lettres : "))
decale(mot, decalage)
