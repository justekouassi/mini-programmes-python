def Echange(dico):
    cles = list(dico.keys())
    nDico = {}
    for i in range(len(cles)):
        nDico[dico[cles[i]]] = cles[i]
    return nDico


dico = {1: "Lundi", 2: "Mardi", 3: "Mercredi",
        4: "Jeudi", 5: "Vendredi", 6: "Samedi", 7: "Dimanche"}
print(Echange(dico))
