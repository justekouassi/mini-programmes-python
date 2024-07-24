# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:10:10 2019

@author: ELIE
"""

n = int(input("Entrez un entier naturel n = "))
n0 = n
H = ['A', 'B', 'C', 'D', 'E', 'F']
n_en_base_k = ""
while n != 0:
    r = n % 16
    if n % 16 > 9:
        a = H[r-10]
    n_en_base_k = str(a) + n_en_base_k
    n = n // 16
print(n0, "exprimé en base ", 16, "vaut : ", n_en_base_k)


n = int(input("Entrez un entier naturel n = "))
n0 = n
k = 16
H = ['A', 'B', 'C', 'D', 'E', 'F']
n_en_base_k = ""
while n != 0:
    a = n % k
    n = n // k
    n_en_base_k = H[n-10] + n_en_base_k
print(n0, "exprimé en base ", k, "vaut : ", n_en_base_k)
