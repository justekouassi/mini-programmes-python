while 1:
    j = t = m = h = s = 0
    t = input("\n\n\n\n\n\tentrez la valeur du temps: ")
    t = int(t)
    m = int(t / 60)
    s = t % 60
    h = int(m / 60)
    m = m % 60
    j = int(h / 24)
    h = h % 24
    print("\n\n", j, "jours", h, " heures", m, "minutes et", s, "seconde")
