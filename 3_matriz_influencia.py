import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matriz_simetrica/matriz_sim_1026_1101.csv", header=None)  # aqui se lee una tabla sin encabezado ni enumeracion 
m= matriz.to_numpy()
l = len(m[:, 0])
G = nx.DiGraph(matriz.values)

def no_caminos(G, fuente, objetivo):
    try:
        n = nx.shortest_path_length(G, fuente, objetivo)
        return(n)
    except nx.NetworkXNoPath:
       return ('No path')

def camino(G, fuente, objetivo):
    mis_caminos = no_caminos(G, fuente, objetivo)
    if mis_caminos == "No path":
        cam = []
    else:
        cam= nx.dijkstra_path(G, fuente, objetivo)
    return(cam)


def peso(path):
    d = len(path)
    if d == 0:
        n = 0
    else:
        n= 0
        for i in range(0, d-1):
            a= path[i]
            b= path[i+1]  
            n= n + m[a, b]
    return(n)

m2 = np.zeros((582, 582))
for i in range(0,l):
    for j in range(i,l):
        path = camino(G, i,j)
        influencia = peso(path)
        m2[i,j] = influencia
        m2[j,i] = influencia
        print(i,j)

pd.DataFrame(m2).to_csv("influencia_1026_1101.csv")



