def Occurence(chaine, char):
    n = 0
    for i in range(len(chaine)) :
        if chaine[i] == char:
            n += 1
    return n

chaine = input("Saisissez la chaine de caractères : ")
char = input("Saisissez le caractère à rechercher : ")

print("'{}' apparaît {} fois \
dans la chaîne '{}'.".format(char, Occurence(chaine,char), chaine))
