from nodo import Nodo

class ListaCircualar():

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None
    
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero
    
    def remover_inicio(self):
        if self.vacia():
            print('Lista vacia')
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def remover_final(self):
        if self.vacia():
            print('Lista vacia')
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break