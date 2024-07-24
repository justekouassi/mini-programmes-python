scrabble = ['A', 1, 'B', 3, 'C', 3, 'D', 2, 'E', 1, 'F', 4, 'G', 2, 'H', 4,
            'I', 1, 'J', 8, 'K', 10, 'L', 1, 'M', 2, 'N', 1, 'O', 1, 'P', 3,
            'Q', 8, 'R', 1, 'S', 1, 'T', 1, 'U', 1, 'V', 4, 'W', 10, 'X', 10,
            'Y', 10, 'Z', 10]


def Valeur(lettre):
    """ renvoie le nombre de points associé à une lettre
    """
    return (scrabble[scrabble.index(lettre)+1])


def MaxiLettre(liste):
    """ renvoie la lettre qui rapporte le plus grand nombre de points.
    Lorsque plusieurs lettres correspondent à la valeur maximale, 
    la fonction renvoie celle qui a le plus grand indice dans liste.
    """
    return max([Valeur(i) for i in liste])


def ValeurMot(mot):
    """ renvoie le nombre total de points du mot (en additionnant les valeurs 
    attribuées à chaque lettre du mot)
    """
    return sum([Valeur(i) for i in mot])


def CompteCarac(mot, lettre):
    """ renvoie le nombre d'occurrences de lettre dans mot.
    """
    return mot.count(lettre)


def Verif(jeu, mot, lettre):
    """ 
    jeu -- liste de lettres majuscules (les lettres dont dispose le joueur)
    mot -- chaîne de caractères (constituée de lettres majuscules, mot que voudrait écrire le joueur) 
    lettre -- une lettre majuscule (lettre disponible sur le plateau de jeu)

    renvoie True si on peut écrire mot avec les lettres de jeu et le caractère lettre, 
    renvoie False sinon.
    """
    jeu.append(lettre)
    for i in jeu:
        if jeu.count(i) >= mot.count(i):
            continue
        else:
            return False
    return True


print(Verif(['A', 'R', 'B', 'E'], "ARBRE", 'E'))
