msg = input("Votre message codé en ASCII : \n")
temp = msg.split()
texte = ""
for i in temp:
    if len(i) == 2:
        texte += chr(int(i))
    else:
        texte += chr(int(i, 2))

print(texte)
