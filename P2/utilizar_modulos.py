# 1er utilizar los modulos 
import modulos

modulos.borrarPantala()
modulos.funcion1()

nom="Daniel"
ape="Carreon"


name, lastname=modulos.funcion4(nom,ape)
print(f"Nombre: {name}\nApellidos:{lastname}")

#2da formar de utilizar modulos
from modulos import borrarPantala, funcion1, funcion4

modulos.borrarPantala()
modulos.funcion1()

nom="Daniel"
ape="Carreon"


name, lastnamme=modulos.funcion4(nom,ape)
print(f"Nombre: {name}\nApellidos:{lastname}")