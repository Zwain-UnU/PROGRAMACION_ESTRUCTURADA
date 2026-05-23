'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
print("\033c")


print("Con prints:")

tabla = int(input("Ingresa una tabla de multiplicar: "))

print(f"{tabla} x 1 = {tabla * 1}")
print(f"{tabla} x 2 = {tabla * 2}")
print(f"{tabla} x 3 = {tabla * 3}")
print(f"{tabla} x 4 = {tabla * 4}")
print(f"{tabla} x 5 = {tabla * 5}")
print(f"{tabla} x 6 = {tabla * 6}")
print(f"{tabla} x 7 = {tabla * 7}")
print(f"{tabla} x 8 = {tabla * 8}")
print(f"{tabla} x 9 = {tabla * 9}")
print(f"{tabla} x 10 = {tabla * 10}")



num_tabla = int(input("Dame un numero para obtener la tabla de multiplicar"))
num = 1
multi = num_tabla * num
print(f"{num_tabla} X {num} = {multi}")
num+=1
#lo de arriba se repite con cada tabla







print("for:")

for num in range (0,101,10):
  multi = num_tabla * num
  print(f"{num_tabla} X {num} = {multi}")
  num+=1

print("while:")


i=1
while i<=10:
  multi = num_tabla * num
  print(f"{num_tabla} X {num} = {multi}")
  i+=1
  num+=1



print("Funcion + estructura")
def tabla(num_tab, n):
    mul = num_tab*n
    print(f"{num_tab} x {n} = {mul}")
    n+=1
    return n


for i in range(1,11):
  num=tabla(num_tabla, num)


 
  