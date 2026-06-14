"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo
 un mismo nombre, para acceder a los valores se hace 
 con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas

paises=["Mexico", "Canada", "EUA","Mexica", "Brasil"]
numeros=[23,45,8,24]
varios=[33, 3.1416, "hola", True]
vacio=[]


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)


#Recorrer la lista 
#1er forma 

for i in (paises):
    print(i)

# #2do forma 
for i in range(0, len(paises)):
    print(paises[i])


#Ordenar los elementos de una lista
print(paises)
paises.sort() #Ordenar los datos de la lista
print(paises)


#EL SORT ORDENA LOS DATOS POR JERARQUIA;
#  COMO SON TEXTOS
#ES POR ABECEDARIO


#dar la vuelta a una lista
paises.reverse()
print(paises)

#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("ONDURAS")
print(paises)

#2da forma
paises.insert(1, "Colombia")
print(paises)
paises.insert(8, "Polonia")
print(paises)
paises[1]=2
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises=["Mexico", "Canada", "EUA","Mexica", "Brasil"]
print(paises)
paises.pop(3)
print(paises)


#2da forma 
paises.remove("EUA")
print(paises)


#Buscar un elemento dentro de la lista
encontro = "EUA" in paises
print(encontro)

#Contar el numeros de veces que aparece un elemento dentro de una lista

numeros=[23,45,8,24,23,100,23]
paises=["Mexico", "Canada", "EUA","Mexica", "Brasil"]


num_veces = numeros.count(23)
print(f"El valor 23 aparece {num_veces} veces.")

num_veces  = paises.count("Mexico")
print(f"El valor mexico aparece {num_veces}.")



#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises=["Mexico", "Canada", "EUA","Mexico", "Brasil"]
posicion = paises.index("Mexico")
print(f"La posicion es {posicion}")

for i in range(0, len(paises)):
    if paises[i]=="Mexico":
        posicion=i
        print(f"Encontre el valor en la posicion: {posicion}")
    

#Unir el contenido de una lista dentro de otra lista
numeros1=[23,45,8,24,23,100,23]
numeros2=[100, -100]
print(numeros1)
print(numeros2)

numeros1.extend(numeros2)
print(numeros1)


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numeros1.sort()
numeros1.reverse()
print(numeros1)


