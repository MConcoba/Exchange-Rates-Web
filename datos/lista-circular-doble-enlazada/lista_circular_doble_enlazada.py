from nodo import Nodo

class ListaCicularDobleEnlazada():

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_inicio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos__()

    def agregar_final(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos__()

    def eliminar_inicio(self):
        if self.vacio():
            print('Lista vacia')
        elif self.primero == self.ultimo:
            self.primero = self.primero = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos__()

    def eliminar_final(self):
        if self.vacio():
            print('Lista vacia')
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unir_nodos__()

    def buscar(self, dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
                    break

    def __unir_nodos__(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def recorrer_incio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break