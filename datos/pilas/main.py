from os import system

system('clear')

from pila import Pila

pila = Pila(5)

pila.push(23)
pila.push(90)
pila.push(45)

pila.show()
