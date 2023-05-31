import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matrices/matriz_1102_1108.csv", header=None)  # aqui se lee una tabla sin encabezado ni enumeracion 
m= matriz.to_numpy()


ageb1_1 = []
ageb2_1= []
tipo_1 = []
peso_1 =[]

ageb1_2 = []
ageb2_2= []
tipo_2 = []
peso_2 =[]

ageb1_3 = []
ageb2_3 = []
tipo_3 = []
peso_3  = []

for i in range(0, len(m[:,0])):
    for j in range(i, len(m[:,0])):
        if m[i,j] > 0 or m[j,i] > 0:
            ageb1_3.append(i+1)
            ageb2_3.append(j+1)
            tipo_3.append("Undirected")
            peso_3.append(m[i,j] +  m[j,i])

red_3 ={'Source': ageb1_3, 'Target': ageb2_3, 'Type':tipo_3,  'Weight':peso_3 }
red_3 = pd.DataFrame(red_3)
red_3.to_csv("red_3_1102_1108.csv")

for i in range(0, len(m[:,1])):
    p=  len(m[:,1]) -1 -i
    q= 0
    for j in range(i, len(m[:,1])):
        if m[i,j] > 0:
            ageb1_1.append(i+1)
            ageb2_1.append(j+1)
            tipo_1.append("Directed")
            peso_1.append(m[i,j])
        if m[p,q]> 0:
            ageb1_2.append(p+1)
            ageb2_2.append(q+1)
            tipo_2.append("Directed")
            peso_2.append(m[p,q])
        q= q + 1
    
      
red_1 ={'Source': ageb1_1, 'Target': ageb2_1, 'Type':tipo_1, 'Weight':peso_1 }
red_1=pd.DataFrame(red_1)
red_1.to_csv("red_1_1102_1108.csv")



red_2 ={'Source':  ageb1_2, 'Target': ageb2_2, 'Type':tipo_2, 'Weight':peso_2 }
red_2=pd.DataFrame(red_2)
red_2.to_csv("red_2_1102_1108.csv")
    
    

