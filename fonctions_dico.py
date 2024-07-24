def trierMots(document):
    """ trier les mots du dico dans l'ordre alphabétique
    """
    fichier = open(document, "r", encoding='utf-8')
    liste = fichier.readlines()
    liste.sort()
    fichier.close()
    fichier = open(document, "w")
    for i in range(0, len(liste)):
        fichier.write(liste[i])
    fichier.close()


def arranger(document):
    fichier = open(document, "r")
    content = fichier.read().replace(" ", "\n")
    fichier.close()

    fichier = open(document, "w")

    for i in range(0, len(content)):
        fichier.write(content[i])
    fichier.close()


def majusculeDico(document):
    """ mettre chacun des mots du dico en majuscule
    """
    fichier = open(document, "r")
    liste = fichier.readlines()
    fichier.close()

    for i in range(0, len(liste)):
        liste[i] = liste[i].upper()

    fichier = open(document, "w")
    for i in range(0, len(liste)):
        fichier.write(liste[i])
    fichier.close()


def doublon(document):
    fichier = open(document, "r")
    liste = fichier.readlines()
    liste2 = []
    fichier.close()

    i = 0
    while i < len(liste):
        liste2.append(liste[i])
        if i == len(liste)-1:
            break
        if liste[i+1] == liste[i]:
            i += 1
        i += 1

    ecrire(liste2)


def ecrire(liste):
    fichier = open(document, "w")
    for i in range(0, len(liste)):
        fichier.write(liste[i])
    fichier.close()


def dix_lettres(document):
    """ prend un dictionnaire et ne garde que les mots de 10 lettres
    """
    fichier = open(document, "r")
    liste = fichier.readlines()
    fichier.close()
    fichier2 = open(" ", "w")
    for mot in liste:
        if len(mot) == 11:
            fichier2.write(mot)
    fichier2.close()


# Saisissez ici le nom du document à traiter
document = ""

# Décommentez le traitement que vous souhaitez utiliser
# trierMots(document)
# arranger(document)
# majusculeDico(document)
# doublon(document)
# dix_lettres(document)
