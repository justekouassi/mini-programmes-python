# Compter le nombre de mots d'une phrase

def OccurenceMot(phrase):
    if len(phrase) == 0:
        return 0
    else:
        i, comp = 0, 0
        while i < len(phrase):
            if phrase[i] == ' ' or phrase[i] == "'" or i == len(phrase)-1:
                comp += 1
            i += 1
        return comp


phrase = input("Entrer la phrase : ")

print("Il y a ", OccurenceMot(phrase), "mot(s) dans la phrase :\n", phrase)
