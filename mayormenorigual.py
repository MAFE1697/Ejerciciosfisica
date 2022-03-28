#!/usr/bin/env python
# coding: utf-8

# Estudiante Maria Fernanda Agreda

# Trabajo de física

# Ejercicio de variables

# Primer número 1

# Ingresar tres Datos y decir cual es el mayor menor igual 1 2 3 1 1 3 3 1 1 1 2 2

# In[6]:


datouno = 3
datodos = 1
datotres = 1

if datouno < datodos and datodos < datotres:
    print('el dato1 es menor que dato2 y dato2 es menor que dato3')
          
elif datouno == datodos and datodos < datotres:
     print('dato1 y dato2 son iguales, dato3 es mayor')
        
elif datouno > datodos and datodos == datotres:
     print('dato1 es mayor, dato2 y dato3 son iguales')

elif datouno < datodos and datodos == datotres:
    print('dato1 es menor, dato2  y  dato3 son iguales')

else:
    print('todos son iguales')
      
         

      
    


# In[ ]:


Esto se conoce como un bucle diccionario de datos


# In[11]:


num = [4, 78, 84, 67]
for n in num:
    print(n)


# In[17]:


valores = { 'A':4,'B':45,'C':16,'D':78 }
for key in valores:
    print(key)


# In[23]:


valores = { 'A':4,'B':45,'C':16,'D':78 }
for valores in valores.values():
    print(valores)


# un ciclo por rango

# In[27]:


for i in range(11):
   print (i)


# In[1]:


for i in range (1,11):
    print(i)


# In[ ]:




