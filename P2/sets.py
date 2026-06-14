"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""


print("\033c")

set1 = {"Hola", "123", "123", "Mexico", "Holanda", 123, 3.1416}


print(set1)

set1.add("Ganador")
print(set1)

set1.pop()
print(set1)

#ejemplo Crear un programa que solicite los email de los
# alumnos de la UTD almacenar en una lista y posteriormente
# mostrar en pantalla los email sin duplicados





#Solucion 1
emails = []
resp=True

while resp:
    
    emails.insert(0,input("Email: ").strip())

    resp=input("Registrar otro email? (si/no)").lower()
    if resp == "no":
        resp=False

email_set=set(emails)
emails=list(email_set)
print(emails)


#Solucion 2

correos = set()

cantidad = int(input("\n¿Cuántos correos desea capturar?: "))

for i in range(cantidad):
    correo = input(f"Correo {i+1}: ")
    correos.add(correo)

print("\nCorreos registrados sin duplicados:")
for correo in correos:
    print(correo)

  



