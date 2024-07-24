def trouve(chaine: str, char: str) -> int:
    for i in range(len(chaine)):
        if chaine[i] == char:
            return i+1
    return -1


chaine = input("Saisissez la chaine de caractere : ")
char = input("Saisissez le caractère à rechercher : ")

print(f"'{char}' se trouve à la position {trouve(chaine, char)}")
