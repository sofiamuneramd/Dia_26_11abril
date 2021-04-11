# Importamos la libreria pandas y por facilidad la abreviamos como pd

import pandas as pd

# Con ExcelFile abrimos el archivo que vamos a usar

File=pd.ExcelFile('Libro1.xls')

# Ahora leemos la hoja en la que se está trabajando 

hoja1=File.parse('Hoja1')

# Leemos los datos de la columna Números y le asignamos una variable para usarla luego

numeros=hoja1['Números'].values

# Un objeto series es un vector con datos indexados 

tamaño0=pd.Series(numeros)

# Vamos que imprime un vestor con los datos de la Hoja1

print(tamaño0)

# Podemos asignar indices

tamaño1=pd.Series(numeros, index=['A','B','C','D','E'])

print(tamaño1)

# Una serie contiene datos en un objeto de tipo Numpy array

print(tamaño1.values)

# El indice en un objeto de tipo index de pandas

print(tamaño1.index)


# Ahora importamos Excel writer para poder crear un libro y hoja nueva

from pandas import ExcelWriter

# Guardamos ambos archivos 

file=ExcelWriter('Copia1.xls')
tamaño0.to_excel(file,'Hoja1')
tamaño1.to_excel(file,'Hoja2')
file.save()



File=pd.ExcelFile('Libro2.xls')

hoja1=File.parse('Hoja1')

paises=hoja1['Paises'].values
print(paises)

# Vamos a asignar una variable a cada elemento de la columna 

a=paises[0]
b=paises[1]
c=paises[2]
d=paises[3]
e=paises[4]

# Creamos un diccionarios con las variables y sus capitales

capitales={a:'Ottawa',b:'Ciudad de México',c:'Bogotá',d:'Madrid',e:'Moscú'}

# Asignamos una serie a partir del diccionario

pd.Series(capitales)

# Guardamos la serie en un archivo nuevo 

file=ExcelWriter('Copia2.xls')
tamaño0.to_excel(file,'Hoja1')
file.save()











