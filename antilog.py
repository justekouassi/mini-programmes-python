import glob
import os.path

print("--PROGRAMME DE SUPPRESSION DE LOG--")
# input("\nVoulez vous supprimer tous les fichiers .log ?")


def listdirectory(path):
    fichier = []
    l = glob.glob(path + "\\*")

    for i in l:
        if os.path.isdir(i):
            fichier.extend(listdirectory(i))
        else:
            fichier.append(i)
    return fichier


for fichier in listdirectory("c:"):
    if os.path.isfile(fichier) and fichier.endswith("log"):
        try:
            os.remove(fichier)
            print(fichier, "[SUPPRIME]")
        except:
            print("impossible de supprimer", fichier)

input("\nLES FICHIERS LOGS ONT ETE SUPPRIMES")
