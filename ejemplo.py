import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

semana= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/semanas_L/1102_1108_L.csv") # lectura de los datos
iid = semana.iloc[:,0]
iid_u = iid.unique()

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

s = semana[semana["id"] == iid_u[0]]


print(agebs_orden(s))



 
