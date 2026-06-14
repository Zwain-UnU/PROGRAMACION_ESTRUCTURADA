print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[23, 73, 45, 8, 24, 0, 100]
print(numeros)

lista=""
i=0
while i<len(numeros):
    
    #lista=lista+str(i)+", "
    lista+=f" {numeros[i]},"
    i+=1
print("["+lista+"]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Dame la palabra a buscar: ").strip()

encontro = palabra in palabras
if palabra in palabras:
    print(f"Encontre la palabta {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")
if encontro == True:
    print(f"Encontrado: {palabra}")
else:
    print("No encontrado")


#2DA FORMA
 
palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Dame la palabra a buscar: ").strip()

#Bandera:
encontro = False


for i in palabras:
    if i == palabra:
       encontro = True

if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No se encontro la palabra {palabra} en la lista ")



        
#3er FORMA

palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Dame la palabra a buscar: ").strip()

#Bandera:
encontro = False

for i in range (0, len(palabras)):
    if palabras[i]==palabra:
        encontro = True
if encontro:
    print(f"Palabra: {palabra}")
else:
    print("No encontrado")


#4ta FORMA
palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Dame la palabra a buscar: ").strip()

#Bandera:
encontro = False

i=0

while i<len(palabras):
    if palabras[i] == palabra:  # Corregido: se agregó palabras[i] para buscar el texto, no el índice
        encontro = True
    i+=1
if encontro:
    print(f"Encontrado: {palabra}")
else:
    print(f"Palabra {palabra} no encontrado.")


        
#Ejemplo 3 Añadir elementos a la lista

lista = []
lista = ["hola", "que", "tal"]
lista[1] = "Hi"
lista[0] = "Hello"

#Opcion 1: Con una varible logica
true=True

while true:
    lista.append(input("Dame un valor: ").strip())
    # Corregido: evaluamos lo que escribe el usuario para saber si romper el ciclo booleano
    entrada_usuario = input("Ingresa True/False para continuar: ").strip().lower()
    if entrada_usuario != "true":
        true = False
    
true="si"
while true == "si":
    lista.append(input("Dame un valor: ").strip())
    
    true="" # Corregido: vaciamos la variable para obligar al ciclo de abajo a ejecutarse
    while true !="si" and true !="no":
        true=input("Ingresa si/no para continuar: ").strip().lower()
        
print(lista)
valor = input("Dame un valor: ").strip().lower()
lista.append(valor)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda = [
    ["Carlos","6181234567"],
    ["Adrian", "6182332456"],
    ["Luis", "6182223444"]
]

print(agenda)
for i in agenda:
    print(i)
ls=""
for r in range(0, 3):
    for c in range(0,2):
        ls+=f"{agenda[r][c]}, " #EN PYTHON NO SE PUEDE PONER [r, c]
    ls+="\n"
print("["+ls+"]")