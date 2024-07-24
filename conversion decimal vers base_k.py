# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:05:31 2019

@author: ELIE
"""

n = int(input("Entrez un entier naturel n = "))
n0 = n
b = int(input("Base k = "))
n_en_base_k = ""
if b > 9:
	print("mauvaise base choisie")
else:
	while n:
		a = n % b
		n = n // b
		n_en_base_k = str(a) + n_en_base_k
	print(n0, "exprimé en base", b, "vaut :", n_en_base_k)
