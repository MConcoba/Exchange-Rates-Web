from collections import defaultdict
from models.data_saved_model import Data

class CircularDouble():

    def __init__(self):
        self.root = None
        self.first = None
        self.last = None

    def empy(self):
        return self.first == None

    def add(self, info, place):
        if self.empy():
            self.first = self.last = Data(info, is_root=True)
        elif place == 'last':
            node = self.__get_place(info)
            new = self.last
            if float(info['id']) <= float(node.id):
                node.left = self.last = new.next = Data(info, parent=node, is_left=True)
            else:
                node.right = self.last = new.next = Data(info, parent=node, is_right=True)
            self.last.prev = new
        elif place == 'first':
            new = Data(info)
            new.next = self.first
            self.first.prev = new
            self.first = new
        else:
            return 'Error to add element'
        self.__join_nodes__()

    def __get_place(self, value):
        aux = self.first
        while aux:
            temp = aux
            if float(value['id']) <= float(aux.id):
                aux = aux.left
            else:
                aux = aux.right
        return temp
    
    def show_in_order(self, node):
        if node:
            self.show_in_order(node.left)
            print(node.id)
            self.show_in_order(node.right)
        
    def show_pre_order(self, node):
        # Ra, Iz, De
        result = []
        if node:
            result.append(node.id)
            result += self.show_pre_order(node.left)
            result += self.show_pre_order(node.right)
        return result

    def show_post_order(self, node):
        # Iz, Ra, De
        if node:
            self.show_post_order(node.left)
            self.show_post_order(node.right)
            print(node)


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
        for item in self.show_from_init():
            fecha = item['date']
            id = item['id']
            iso = item['iso']
            id = item['id']
            pais = item['country']
            valor = item['value']
            monedas[fecha].append(
                {'id': id, 'iso': iso, 'pais': pais, 'valor': valor})
        dots = self.get_dots()
        resultado = {'status': True,'tree': dots,  'tooltips': [], 'records': [
            {'fecha': fecha, 'monedas': monedas} for fecha, monedas in monedas.items()]}
        return resultado

    def get_lent(self):
        return self.show_from_init().__len__()
    
    def get_dots(self):
        if not self.first:
            return ''
        graph = '\n'
        stack = [self.first]
        while stack:
            node = stack.pop()
            if node:
                graph += f'  {node.id} [tooltip="{node.data}"];\n'
                if node.left:
                    graph += f'  {node.id} -> {node.left.id};\n'
                    stack.append(node.left)
                if node.right:
                    graph += f'  {node.id} -> {node.right.id};\n'
                    stack.append(node.right)
        #graph += '}'
        return graph

    def __join_nodes__(self):
        if self.first != None:
            self.first.prev = self.last
            self.last.next = self.first
