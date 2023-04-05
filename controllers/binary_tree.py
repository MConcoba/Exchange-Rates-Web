
import json
class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        #print(data['id'])
        #print(node.data['id'])
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = BinaryNode(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = BinaryNode(data)
            else:
                self._add(data, node.right)

    def find(self, data):
        if self.root is None:
            return None
        else:
            return self._find(data, self.root)

    def _find(self, data, node):
        if data['id'] == node.data['id']:
            return node
        elif data['id'] < node.data['id'] and node.left['id'] is not None:
            return self._find(data, node.left)
        elif data['id'] > node.data['id'] and node.right['id'] is not None:
            return self._find(data, node.right)
        else:
            return None
        
    def print_inorder(self, node):
        # izquierda- raiz - derecha 
        if node is not None:
            self.print_inorder(node.left)
            print(node.data['id'])
            self.print_inorder(node.right)
    
    def print_postorder(self, node):
        # izquierza - derecha - raiz
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data['id'])

    def print_preorder(self, node):
        # raiz - izquierda - derecha
        if node:
            print(node.data['id'])
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def tooltips(self, node):
        t = f'{node["id"]} [tooltip="{node}"];'
        return t

    def preorder_dot(self, node):
        if node is None:
            return ""
        #1 [tooltip="{'id': '1', 'fecha': '2023-02-07', 'iso': 'JPY', 'pais': 'Japan', 'valor': 132.62}"];
        dot = f"{node.data['id']}"
        #dot += self.tooltips(node)
        if node.left is not None:
            dot += f"->{node.left.data['id']}"
        if node.right is not None:
            dot += f"->{node.right.data['id']}"
        dot += "\n"
        dot += self.preorder_dot(node.left)
        dot += self.preorder_dot(node.right)


        return dot
    
    def new_dot(self, input_str):
        output_lines = []
        for line in input_str.split("\n"):
            nodes = line.split("->")
            if len(nodes) == 2:
                #print(nodes)
                if not nodes[1]:  # Si el nodo derecho está vacío
                    nodes[1] = " "
                elif not nodes[0]:
                    nodes[0] = " "
                output_lines.append("->".join(nodes))
            elif len(nodes) == 3:
                output_lines.append(f"{nodes[0]}->{nodes[1]}")
                output_lines.append(f"{nodes[0]}->{nodes[2]}")
            else:
                output_lines.append(line)

        output_str = "\n".join(output_lines)
        return output_str





class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None