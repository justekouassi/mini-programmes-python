a = 2
b = 1
while 1:
    l = []
    for i in range(2, a):
        if (a % i) != 0:
            l.append(i)
    if len(l) == len(range(2, a)):
        print(a, '\t\t', b)
        b += 1
    a += 1
