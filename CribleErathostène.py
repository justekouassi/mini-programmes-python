liste = [1 for x in range(1001)]

for i in range(2, 1001):
    if liste[i] != 0:
        for j in range(i+1, 1001):
            if j % i == 0:
                liste[j] = 0

premiers = []

for i in range(1, 1001):
    if liste[i] != 0:
        premiers.append(i)

print(premiers)
