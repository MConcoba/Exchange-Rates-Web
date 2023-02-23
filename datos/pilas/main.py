from os import system

#system('clear')

from pila import Pila

pila = Pila(5)

pila.push(23)
pila.push(90)
pila.push(45)
pila.push(100)
pila.push(43)
pila.push(23)
pila.push(41)
pila.push(4124)
pila.push(134)
pila.push(66)
pila.push(11)

pila.pop()

pila.show()

print(f'Size: {pila.Size()}')
print(f'Estado: {pila.empty()}')
print(f'Top: {pila.Top()}')


