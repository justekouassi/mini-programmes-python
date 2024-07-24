from datetime import *

j = 1
while j != 0:
    print("Temps N°", j, '=')
    d = datetime.now()
    input("{:%M mn %S s %f}".format(d))
    print("\n")
    j += 1
