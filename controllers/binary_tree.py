
import json
from models.general_node import GeneralNodo

class BinaryTree:

    def __init__(self):
        self.first = None
        self.last = None

    def empy(self):
        return self.first == None

    def add(self, info):
        print(info)
        if self.empy():
            self.first = self.last = GeneralNodo(info, is_root=True)
        else:
            node = self.__get_place(info)
            new = self.last
            if float(info['id']) <= float(node.data['id']):
                node.left = self.last = new.next = GeneralNodo(info, parent=node, is_left=True)
            else:
                node.right = self.last = new.next = GeneralNodo(info, parent=node, is_right=True)
            self.last.prev = new
    
    def __get_place(self, value):
        aux = self.first
        print(aux.data)
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
    
    def get_dots(self):
        if not self.first:
            return ''
        graph = '\n'
        stack = [self.first]
        while stack:
            node = stack.pop()
            if node:
                formatted_data = "\n".join([f"{key}: {value}" for key, value in node.data.items()])
                graph += f'{node.id} [tooltip="{formatted_data}"];\n'
                if node.left:
                    graph += f'  {node.id} -> {node.left.id};\n'
                    stack.append(node.left)
                if node.right:
                    graph += f'  {node.id} -> {node.right.id};\n'
                    stack.append(node.right)
        #graph += '}'
        return graph


    

      