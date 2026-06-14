"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1 = ("Mexico", "Canada", "EUA")
varios=("Hola", True, 33, 3.1416)

for i in paises1:
    print(i)

for i in range(0,len(paises1)):
    print(paises1[i])

i=0

while i< len(paises1):
    print(paises1[i])
    i+=1

print(f"El pais que inaigura la copa del mundo es: {paises1[0]}")

edades = (23, 24, 18, 20, 23, 24, 19, 24)
print(edades)
cuantos = edades.count(24)
print(cuantos)

#Crear un programa que me lea un numero y me diga en que posicion esta 

encontrar=int(input("Dame el numero a buscar: "))

posicion=edades.count(encontrar)
print(posicion)

#UTILIZANDO SET
posiciones={""}
posiciones.clear()

for i in range(0, len(edades)):
    if edades[i] == encontrar:
      posiciones.add(i)

posiciones=set(posiciones)

for i in posiciones:
    print(f"El numero {encontrar} esta en la posicion: {i}")

for i in edades:
    posicion=edades.index(encontrar)
print(f"Esta en la posicion: {posicion}")


#UTILIZANDO TUPLAS
posiciones=[]

for i in range(0, len(edades)):
    if edades[i] == encontrar:
      posiciones.append(i)
posiciones=tuple(posiciones)
for i in posiciones:
    print(f"El numero {encontrar} esta en la posicion: {i}")

