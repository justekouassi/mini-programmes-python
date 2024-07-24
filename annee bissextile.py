# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:19:31 2019

@author: ELIE
"""

an = int( input("Saisir une année : "))
if ((an%4==0) and (an%100 != 0)) or an%400==0 :
    print (an,"est une année bissextile")
else:
    print (an,"n'est pas une année bissextile" )

a=input()
