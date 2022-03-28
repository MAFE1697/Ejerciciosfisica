#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("NUMEROS PARES E IMPARES")


# In[3]:


print('NUMEROS PARES')
sumapar=0
sumaimpar=0
for n in range (0,10):    
    if  n % 2 ==0:
        print ('pares',n)   
        sumapar=sumapar+1
        
    else:
        print('impares',n)
        sumaimpar=sumaimpar+1
        print(sumapar)

                   
  


# In[1]:


pares=[]
impares=[]

for n in range (1,21):
    print(n)
   
    if  n % 2 ==0:
        pares.append(n)
   
    else:
        impares.append(n)
   
   
print("la cantidad de numeros pares es {}".format(len(pares)))
print("la cantidad de numeros impares es {}".format(len(impares)))


# In[ ]:




