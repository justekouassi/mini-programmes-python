def triBulle(liste: list) -> list:
    echange = True
    while echange:
        echange = False
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                echange = True
    return liste


liste: list[int] = [25, 0, 4, 17, 63, 4, 5, 7, 9, 2, 8, 3, 4]
print(triBulle(liste))
