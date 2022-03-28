# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:56:54 2022

@author: FERNANDA AGREDA
"""

print("*******************************")

Lista = []

for info in range(4):
       nombres= input("Ingrese nombre: ")
       Lista.append(nombres)

       
nom = 0
totalNombres = len(Lista)
print("El total de nombres es: ",totalNombres)

while nom < totalNombres:
    print(Lista[nom])
    nom = nom + 1



   