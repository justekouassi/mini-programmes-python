def chaineListe(phrase):
    phrase = input("Saisissez une phrase : ")
    

Mots = chaineListe(phrase)

k = 0
for i in range(len(Mots)):
    if len(Mots[i]) > len(Mots[k]) :
        k = i

print("Le mot le plus long de votre phrase est :",Mots[k])
