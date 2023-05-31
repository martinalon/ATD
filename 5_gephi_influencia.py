import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matriz_influencia/influencia_1012_1018.csv", header=None)  # aqui se lee una matriz simetrica sin encabezado ni enumeracion 
m= matriz.to_numpy()
d = len(m[:,0])

ageb1 = []
ageb2 = []
tipo = []
peso  = []

for i in range(0, d):
    for j in range(i, d):
        if m[i,j] > 0 :
            ageb1.append(i+1)
            ageb2.append(j+1)
            tipo.append("Undirected")
            peso.append(m[i,j])

red ={'Source': ageb1, 'Target': ageb2, 'Type':tipo,  'Weight':peso}
red = pd.DataFrame(red)
red.to_csv("red_influencia_1012_1018.csv")