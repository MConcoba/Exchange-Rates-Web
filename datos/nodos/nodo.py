class Nodo():
    
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
    
    def __str__(self):
        return str(self.dato)
    
def recorrer(nodo):
    while nodo != None:
        print(nodo.dato)
        nodo = nodo.siguiente

nodo4  = Nodo(12)
nodo3  = Nodo(45, nodo4)
nodo2  = Nodo(67, nodo3)
nodo1  = Nodo(89, nodo2)

recorrer(nodo1)