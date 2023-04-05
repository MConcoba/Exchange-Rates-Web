from collections import defaultdict

from models.data_saved_model import Data
from controllers.binary_tree import BinaryTree
import random


class CircularDouble():

    def __init__(self):
        self.first = None
        self.last = None
        self.tree = BinaryTree()

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

    def delete(self, value):
        current_node = self.first
        while current_node.data != value:
            current_node = current_node.next
            if current_node == self.first:
                return "El elemento no existe"
        if current_node == self.first:
            self.first = current_node.next
            self.first.prev = self.last
            self.last.next = self.first
        elif current_node == self.last:
            self.last = current_node.prev
            self.last.next = self.first
            self.first.prev = self.last
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        return self.show_group_from_init()

    def show_from_init(self):
        lista = []
        aux = self.first
        while aux:
            lista.append(aux.data)
            aux = aux.next
            if aux == self.first:
                break
        return lista

    def clear(self):
        self.first = None
        self.last = None

    def show_group_from_init(self):
        monedas = defaultdict(list)
        tools = []
        for item in self.get_random_list():
            fecha = item['date']
            id = item['id']
            iso = item['iso']
            id = item['id']
            pais = item['country']
            valor = item['value']
            tools.append(self.tree.tooltips(item))
            monedas[fecha].append(
                {'id': id, 'iso': iso, 'pais': pais, 'valor': valor})
        dot = self.tree.preorder_dot(self.tree.root)
        a = self.tree.new_dot(dot)
        resultado = {'status': True,'tree': a,  'tooltips': tools, 'records': [
            {'fecha': fecha, 'monedas': monedas} for fecha, monedas in monedas.items()]}
        return resultado

    def get_random_list(self):
        self.tree = BinaryTree()
        list_random = []
        lista = self.show_from_init()
        random.shuffle(lista)
        nueva_lista = lista
        random.shuffle(nueva_lista)
        for item in nueva_lista:
            self.tree.add(item)
            list_random.append(item)
        return list_random

    def get_lent(self):
        return self.show_from_init().__len__()

    def __join_nodes__(self):
        if self.first != None:
            self.first.prev = self.last
            self.last.next = self.first
