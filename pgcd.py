# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 07:09:50 2019

@author: ELIE
"""


def pgcd_euclide(m, n):
    a = m
    b = n
    while b != 0:
        r = a % b
        a = b
        b = r
    print("Le PGCD de", m, "et", n, "est", a)


def pgcd_recursif(m, n):
    a = m
    b = n
    while a != b:
        if a > b:
            a = a-b
        elif a < b:
            b = b-a
    print("PGCD (", m, ";", n, ") =", b)
