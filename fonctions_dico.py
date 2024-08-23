def trier_mots(document):
    """ Trier les mots du dico dans l'ordre alphabétique """
    with open(document, "r", encoding="utf-8") as fichier:
        liste = fichier.readlines()
    liste.sort()
    ecrire(liste, document)


def arranger(document):
    """ Remplacer les espaces par des nouvelles lignes """
    with open(document, "r", encoding="utf-8") as fichier:
        content = fichier.read().replace(" ", "\n")
    ecrire(content, document)


def majuscule_dico(document):
    """ Mettre chaque mot du dico en majuscule """
    with open(document, "r", encoding="utf-8") as fichier:
        liste = fichier.readlines()
    liste = [mot.upper() for mot in liste]
    ecrire(liste, document)


def doublon(document):
    """ Éliminer les doublons consécutifs dans le fichier """
    with open(document, "r", encoding="utf-8") as fichier:
        liste = fichier.readlines()

    liste2 = []
    for i in range(len(liste)):
        if i == 0 or liste[i] != liste[i - 1]:
            liste2.append(liste[i])

    ecrire(liste2, document)


def dix_lettres(document, output_file="dix_lettres.txt"):
    """ Garder uniquement les mots de 10 lettres """
    with open(document, "r", encoding="utf-8") as fichier:
        liste = fichier.readlines()

    mots_10_lettres = [mot for mot in liste if len(mot.strip()) == 10]
    ecrire(mots_10_lettres, output_file)


def ecrire(contenu, document):
    """ Écrire du contenu dans un fichier """
    if isinstance(contenu, list):
        contenu = "".join(contenu)

    with open(document, "w", encoding="utf-8") as fichier:
        fichier.write(contenu)


# Saisissez ici le nom du document à traiter
document = "votre_document.txt"

# Décommentez le traitement que vous souhaitez utiliser
# trier_mots(document)
# arranger(document)
# majuscule_dico(document)
# doublon(document)
# dix_lettres(document)
