#! /usr/bin/ python
# -*- coding: utf-8 -*

import sys
import string

begin_word = ""
end_word = "\n"


def isnewword(wordsearch):
    isnewword = True
    outfsearch = outf
    outfsearch.seek(0)
    for linesearch in outfsearch:
        if linesearch.find(wordsearch) != -1:
            return False
    if outline.find(wordsearch) != -1:
        return False
    return isnewword


try:
    inf = open(sys.argv[1], "rb")
except IndexError:
    print("erreur ... pas de fichier IN")
    sys.exit()

try:
    outf = open(sys.argv[2], "wb+")
except IndexError:
    outf = open(sys.argv[1] + ".out", "wb+")

for line in inf:
    line = "".join([word if word not in string.punctuation
                    else " " for word in line])
    line = line.lower()
    line = line.split()
    outline = ""
    for word in line:
        word = begin_word + " ".join(word) + end_word
        if isnewword(word):
            outline = outline + word
    outf.write(outline)

inf.close()
outf.close()
