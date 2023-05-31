import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/datos/datos_1109_1115.csv") # lectura de los datos
ids = pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/ids/ids_1109_1115.csv") # lectura de los datos
iid_u = ids.iloc[:,0]
print(len(iid_u))

def datos_sl(datos, iid_u): #esta funcion toma los datos completos de una semana y me regres la informacion de los ids en la tabla de ids
    d = len(iid_u)
    for i in range(0, d):
        b =  datos[datos["id_adv"] == iid_u[i]]
        if i == 0:
            a = b
        else:
            a = pd.concat([a, b], axis=0)
        print(i)
    return(a)

datos_sl = datos_sl(datos, iid_u)

dict = {'id_adv': 'id',
        'timestamp': 'timestamp',
        'lat': 'lat',
        'lon': 'lon'}

datos_sl.rename(columns=dict,
          inplace=True)



datos_sl.to_csv("1109_1115_SL.csv", index = False)