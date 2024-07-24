semaine = ["Lundi", "Mardi", "Mercredi",
           "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s = 3
m = 0
for i in jours:
    for j in range(i):
        print(semaine[s % 7], j+1, mois[m])
        s += 1
    m += 1
