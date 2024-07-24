# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:52:00 2019

@author: ELIE
"""

n = int (input ("Entrez un entier naturel n = "))
n0 = n
n_en_base_k = ""
while n!=0 :
    a= n % 2
    n = n // 2
    n_en_base_k = str(a) + n_en_base_k
print (n0, "exprimé en base 2 vaut : ", n_en_base_k)

def conv_bin(n):
    n0 = n
    n_en_base_k = ""
    while n!=0 :
        a= n % 2
        n = n // 2
        n_en_base_k = str(a) + n_en_base_k
    return n_en_base_k
