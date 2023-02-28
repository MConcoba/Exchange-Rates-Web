from collections import defaultdict

from models.data_saved_model import Data

class CircularDouble():

    def __init__(self):
        self.first = None
        self.last = None

    def empy(self):
        return self.first == None

    def add(self, info, place):
        if self.empy():
            self.first = self.last = Data(info)
        elif place == 'last':
            new = self.last
            self.last = new.next = Data(info)
            self.last.prev = new
        elif place == 'first':
            new = Data(info)
            new.next = self.first
            self.first.prev = new
            self.first = new
        else:
            return 'Error to add element'
        self.__join_nodes__()

    def remove(self, place):
        if self.empy():
            return 'No se tiene informacion que eliminar'
        elif self.first == self.last:
            self.first = self.last = None
        elif place == 'first':
            self.first = self.first.next
        elif place == 'last':
            self.last = self.last.prev
        else:
            return 'Error to delete element'

    def show_from_init(self):
        lista = []
        aux = self.first
        while aux:
            lista.append(aux.data)
            aux = aux.next
            if aux == self.first:
                break
        return lista
    
    def show_group_from_init(self):
        monedas = defaultdict(list)
        for item in self.show_from_init():
            fecha = item['date']
            iso = item['iso']
            pais = item['country']
            valor = item['value']
            monedas[fecha].append({'iso': iso, 'pais': pais, 'valor': valor})
        resultado = {'status': True, 'records': [{'fecha': fecha, 'monedas': monedas} for fecha, monedas in monedas.items()]}
        return resultado
    
    def __join_nodes__(self):
        if self.first != None:
            self.first.prev = self.last
            self.last.next = self.first
