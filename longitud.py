import numpy as np
import scipy
import math
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pyproj

coor= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/datos_semana/datos_1109_1115.csv") # lectura de los datos
iid = coor.iloc[:,0]
#iid_u = iid.unique()

#un_id= coor[coor["id"] == iid_u[0]]
#un_id.to_csv("un_id.csv")

print(len(iid) )


#print("la longitud de cada uno")
#coor1= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/Datos entre semana/datos por semana/1207_1211_reducidos_7_15.csv") # lectura de los datos
#coor2= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/Datos entre semana/datos por semana/1207_1211_reducidos_15_23.csv") # lectura de los datos
#coor3= pd.read_csv("/home/martin/Escritorio/libros del cimat/Tesis/Datos/pyton/Datos entre semana/datos por semana/1207_1211_reducidos_23_7.csv") # lectura de los datos
#print(len(coor1.iloc[:,1]))
#print(len(coor2.iloc[:,1]))
#print(len(coor3.iloc[:,1]))

#print("la suma de longitudes")

#print( len(coor1.iloc[:,1]) + len(coor2.iloc[:,1]) + len(coor3.iloc[:,1]))
