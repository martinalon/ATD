import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from gtda.graphs import GraphGeodesicDistance
from gtda.homology import VietorisRipsPersistence, SparseRipsPersistence, FlagserPersistence
from gtda.plotting import plot_diagram


matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matrices/matriz_1102_1108.csv", header=None)  # aqui se lee una tabla sin encabezado ni enumeracion 
m= matriz.to_numpy()
dim = len(m[:,0])
# m2 sera la matriz de adyacencias, una matriz simetrica
m2= np.zeros((dim, dim))
for i in range(0, dim):
    for j in range(i, dim):
        if m[i,j]> 0 or m[j,i]> 0:
            peso = (m[i,j]+m[j,i])
            m2[i,j] = peso
            m2[j,i] = peso
            
pd.DataFrame(m2).to_csv("matriz_sim_1102_1108.csv")