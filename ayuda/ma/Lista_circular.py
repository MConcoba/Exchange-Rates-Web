from nodo import Nodo
import random


class listacircular():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
            return self.primero == None
    
    def agregarinicio(self, fecha, moneda, cambio):
        nuevo_id = 5
        if not self.vacia():
            # Generar un nuevo id aleatorio y comprobar que no se encuentre en la lista
            while True:
                nuevo_id = random.randint(1, 100)
                if not self.buscar_id(nuevo_id):
                    break
        nuevo_nodo = Nodo(nuevo_id, fecha, moneda, cambio)
        if self.vacia():
            self.primero = self.ultimo = nuevo_nodo
            self.ultimo.siguiente = self.primero
        else:
            aux = nuevo_nodo
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def agregarFinal(self,fecha,moneda,cambio):
        id = 0
        if self.vacia():
            self.primero =self.ultimo = Nodo(id, fecha,moneda,cambio)
            self.ultimo.siguiente =self.primero
        else:
            aux = self.ultimo
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        listado = []
        while aux:
            #print("id: "+str(aux.id)+" Fecha de cambio: " + str(aux.fecha) + " Moneda " +  str(aux.moneda) + " " +  str(aux.cambio))
            info = str(aux.id), str(aux.fecha), str(aux.moneda), str(aux.cambio)
            listado.append(info)
            aux = aux.siguiente
            if aux == self.primero:
                break
        return listado
    
    def buscar_id(self, id_buscar):
        aux = self.primero
        while aux:
            if aux.id == id_buscar:
                return True
            aux = aux.siguiente
            if aux == self.primero:
                break
        return False


