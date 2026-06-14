from paquete1 import modulos,modulo_paquete

modulos.borrarPantala()
modulos.funcion1()

nom="Daniel"
ape="Carreon"
edad=modulo_paquete.edad()

name,lastname=modulos.funcion4(nom,ape)
men=modulo_paquete.funcion4(nom,ape,edad)

print(f"Name: {name}\nLastname: {lastname}\nEdad:{edad}")
print(men)