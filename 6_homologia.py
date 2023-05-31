import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from gtda.graphs import GraphGeodesicDistance
from gtda.homology import VietorisRipsPersistence, SparseRipsPersistence, FlagserPersistence
from gtda.plotting import plot_diagram


matriz= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/matriz_simetrica/matriz_sim_0928_1004.csv", header=None)  # aqui se lee una tabla sin encabezado ni enumeracion 
m= matriz.to_numpy()  # esta es una matriz simetrica


def matriz_h1(m):   # esta es la matriz que se utilizara para hacer el estudio de la homogia cuya filtracion va del menor flujo de gente al mayor
    dim = len(m[:,0])
    m2= np.zeros((dim, dim))
    for i in range(0, dim):
        for j in range(i, dim):
            if m[i,j]> 0 :
                m2[i,j] = m[i,j]
                m2[j,i] = m[j,i]
            else:
                m2[i,j] = np.inf
                m2[j,i] = np.inf
                
    for i in range(0, dim):
        m2[i,i] = 0
    return(m2)


def matriz_h2(m):   # esta es la matriz que se utilizara para hacer el estudio de la homogia cuya filtracion va del mayor flujo de gente al manor
    dim = len(m[:,0])
    m2= np.zeros((dim, dim))
    for i in range(0, dim):
        for j in range(i, dim):
            if m[i,j]> 0 :
                m2[i,j] = 1/ m[i,j]
                m2[j,i] = 1/m[j,i]
            else:
                m2[i,j] = np.inf
                m2[j,i] = np.inf
                
    for i in range(0, dim):
        m2[i,i] = 0
    return(m2)



# m2 sera la matriz de adyacencias, una matriz simetrica
#m2= np.zeros((dim, dim))
#for i in range(0, dim):
#    for j in range(i, dim):
#        if m[i,j]> 0 or m[j,i]> 0:
#            peso = (m[i,j]+m[j,i])
#            m2[i,j] = peso
#            m2[j,i] = peso
#        else:
#            m2[i,j] = np.inf
#            m2[j,i] = np.inf

#for i in range(0, dim):
#    m2[i,i] = 0


matrizh = matriz_h2(m)


X = [matrizh]

# Instantiate topological transformer
VR = VietorisRipsPersistence(metric="precomputed")
print(VR)

# Compute persistence diagrams corresponding to each entry (only one here) in X
diagrams = VR.fit_transform(X)


def max_intervalo(diagrams):
    n = diagrams[0,:, 1]
    dim = len(n)
    for i in range (0, dim):
        idx = n.argsort()[-(i+1)]
        if n[idx] != np.inf: 
            break
    return(n[idx])
            
second_max = max_intervalo(diagrams)   # aqui desaparece el ultimo intervalo antes de ser inf 

print(len(diagrams[0]))
for i in range(0, len(diagrams[0])):
    diagrama = diagrams[0,i]
    a= diagrama[0]
    b= diagrama[1]
    c= diagrama[2]
    if b == np.inf:
        b= second_max + 0.2
        if c == 0:
           color = "red"
        elif c == 1:
            color = "green"
        else:
            color = "blue"
        dominio = [a,b]
        imgaen  = [i,i]
    else:
        if c == 0:
           color = "red"
        elif c == 1:
            color = "green"
        else:
            color = "blue"
        dominio = [a,b]
        imgaen  = [i,i]
    plt.plot(dominio, imgaen, color= color)

H0 =  mpatches.Patch(color='red', label='H0')
H1 =  mpatches.Patch(color='green', label='H1')

plt.legend(handles=[H0, H1])
plt.show()

VR.plot(diagrams, sample=0).show()
