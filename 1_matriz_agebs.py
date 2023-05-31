import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

semana= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/semanas_L/1102_1108_L.csv") # lectura de los datos
iid = semana.iloc[:,0]
iid_u = iid.unique()
print(len(iid_u))

#################################################  funcion para ordenar agebs
# df: tiene que ser un data frame
def agebs_orden(df):                                     # La función toma todos los datos de un mismo id y regresa un data frame con los agebs que visita  acomodados por el tiempo. 
    ageb0 = df.iloc[:,4]                                 # Estos son los agebs que aun no se acomodan en orden de tiempo
    tiempo0 = df.iloc[:,1]                               # Esta es la columna con la informacion del tiempo en donde cada elemento tiene formato  string
    tiempo0= tiempo0.array
    dim = len(tiempo0)                                   # Esta es el numero de veces que aparece el ID preseleccionado
    tiempo = []                                          # Este sera un arreglo que se llenara con la informacion del tiempo pero ya como variables tipo timestamp
    for i in range(0, dim):                              # Este ciclo permitirá cambiar los datos de tiempo de formato string a timestamp
        t_0= pd.Timestamp( str(tiempo0[i])[0:19])              
        tiempo.append(t_0)
    datos={ 'tiempo': tiempo, 'ageb': ageb0}             # Con esto creo un nuevo data frame cuyas culumnas son (tiempo en fomato timestamp, ageb en enteros)
    datos=pd.DataFrame(datos)                              
    datos.sort_values(by=['tiempo'], inplace=True)       # con esto reacomodo en nuevo data frame datos de acuerdo al tiempo en manera acendente   
    return(datos.iloc[:,1])
#####################################################################################################################################################
################################################    Funcion para contar los saltos entre agebs
# agebs: tiene que ser un arreglo
# matriz: es la matriz de 582 por 582 que se ira actualizando 
def M(agebs, matriz):                                    
    for i in range(1, len(agebs)):           
        a= agebs[i-1]                             
        b= agebs[i]
        if a!= b:
            matriz[a - 1, b-1 ] = matriz[a-1, b-1] + 1  # recordar que en python la iteracion comienza en cero y la matriz de agebs comienza en 1, por ello a los agebs les resto 1 
    return(matriz)



matriz = np.zeros((582, 582))
for i in range(0, len(iid_u)):
    tid= semana[semana["id"] == iid_u[i]]                  # esto me regresa las filas que tengan el mismo id. Las columnas son (id, timestamp, lat, lon, ageb)
    agebs = agebs_orden(tid)
    agebs = agebs.array
    mi_M = M(agebs, matriz)
    matriz= mi_M 
    print( i )
    
pd.DataFrame(matriz).to_csv("matriz_1102_1108.csv")

    



