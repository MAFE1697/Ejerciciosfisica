# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:29:31 2022

@author: FERNANDA AGREDA
"""
codigo=['1','2']
nombres= ['Juan','Carlos']
apellidos=['Paz','Ruiz','Lopez']
cargo=['Ing Sistemas', 'Enfermero']
telefono= [3215669955,3145666887]


menuprincipal = int(input("Menu Principal: \n 1- Ver Menu \n 2- Insertar Datos \n 3- Eliminar Dato \n 4- Modificar Datos \n 5- Organizar Datos \n 0- SAlir \n"))

while menuprincipal !=0:
    
   if menuprincipal == 1:
      print("Codigo de la persona: ")
   for x in range(len(codigo)):
        print(codigo[x]," ",    nombres[x]," ",    apellidos[x]," ",    cargo[x]," ",    telefono[x], " ") 
               
   if menuprincipal == 2:
        print("Escriba los siguientes datos:")
        codigo.append(input("Codigo de la persona: "))
        nombres.append(input("Nombres de la persona: "))
        apellidos.append(input("Apellidos de la persona: "))
        cargo.append(input("Cargo: "))
        telefono.append(int(input("Telefono de la persona: ")))
        
   elif menuprincipal == 3:       
       cod=input("Ingresa el codigo que deseaas eliminar:  ")
       for i in range(len(codigo)-1,-1,-1):
            if codigo[i]== cod:
                codigo.pop(i)
                nombres.pop(i)
                apellidos.pop(i)
                cargo.pop(i)
                telefono.pop(i)
            print("Persona eliminada")
              
   elif menuprincipal == 4:
        print("Modificar Dato") 
        cod= input("Ingresa el codigo a modificar: ")        
        for x in range(len(codigo)):
          if codigo[x]==cod:
              nombres[x]= input("Cual es el nuevo nombre?: ")
              apellidos[x]= input("Cual es el nuevo apellido?: ")
              cargo[x]= input("Cual es el nuevo cargo?: ")
              telefono[x]=int (input("Cual es el nuevo numero telefonico?: "))
        print("Persona modificada")
    
   elif menuprincipal == 5:
         print("Organizar los Datos") 
         cod= input("Ingresa el dato a organizar: ")
         codigo.sort()
         print(codigo)

    
   else:    print("Por favor digita una opcion correcta")
  
   menuprincipal = int(input("Menu Principal: \n 1- Ver Menu \n 2- Insertar Datos \n 3- Eliminar Dato \n 4- Modificar Datos \n 5- Organizar Datos \n 0- SAlir \n"))
