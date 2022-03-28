# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:20:32 2022

@author: FERNANDA AGREDA
"""

nombres=[]
apellido=[]
apellidos=[]


for x in range(2):
   nom= input("Ingrese el  nombre: ")
   nombres.append(nom)
   
   ape1= input("Ingrese el  primer apellido: ")   
   ape2= input("Ingrese el segundo apellido: ")
   apellidos.append([ape1,ape2])
   
for x in range(2):
    print(nombres[x],apellido[x][1],apellido[x][1])
   
  
            