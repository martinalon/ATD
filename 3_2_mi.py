import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matriz_simetrica/matriz_sim_1102_1108.csv", header=None)  # aqui se lee una tabla sin encabezado ni enumeracion 
m= matriz.to_numpy()
l = len(m[:, 0])
G = nx.DiGraph(matriz.values)

def existe(G, fuente, objetivo):    # esta funcion me regresa true si existe camino entre los dos nodos y false  si no lo hay.
    m = nx.has_path(G, fuente, objetivo)
    return(m)
 

def shortest(G, fuente, objetivo):  # esta funcion me regresa ruta y el peso del camino mas corto entre dos vertices contando el peso
    s_c = nx.dijkstra_path(G, fuente, objetivo)
    s_v = nx.dijkstra_path_length(G, fuente, objetivo)
    return(s_c, s_v)

m2 = np.zeros((582, 582))
for i in range(0, l):
    for j in range(i, l):
        existencia = existe(G, i, j)
        if existencia == False:
            m2[i,j] = 0
            m2[j,i] = 0
        else:
            arr, v = shortest(G, i, j)
            m2[i,j] = v
            m2[j,i] = v
        print(i,j)
        
pd.DataFrame(m2).to_csv("influencia_1102_1108.csv")
            





            
    


