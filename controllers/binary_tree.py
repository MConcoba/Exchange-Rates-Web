
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
    
    def preorder_list(self, node):
        # raiz - izquierda - derecha
        result = []
        if node:
            result.append(node.data['id'])
            result += self.preorder_list(node.left)
            result += self.preorder_list(node.right)
        return result

    def tooltips(self, node):
        t = f'{node["id"]} [tooltip="{node}"];'
        return t

    def preorder_dot(self, node):
        graph = ''
        stack = [node]
        while stack:
            node = stack.pop()
            if node:
                #graph += f'  {node.data} [label="{node.data}"];\n'
                if node.left:
                    graph += f'  {node.data["id"]} -> {node.left.data["id"]}\n'
                    stack.append(node.left)
                if node.right:
                    graph += f'  {node.data["id"]} -> {node.right.data["id"]}\n'
                    stack.append(node.right)
        
        return graph

        """ if node is None:
            return ""
        dot = f"{node.data['id']}"
        if node.left is not None:
            dot += f"->{node.left.data['id']}"
        if node.right is not None:
            dot += f"->{node.right.data['id']}"
        dot += "\n"
        dot += self.preorder_dot(node.left)
        dot += self.preorder_dot(node.right)


        return dot """
    
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
    

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if not node:
            return BinaryNode(key)
        elif key < node.data:
            node.left = self._insert_helper(node.left, key)
        else:
            node.right = self._insert_helper(node.right, key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.data:
            return self._rotate_right(node)

        if balance < -1 and key > node.right.data:
            return self._rotate_left(node)

        if balance > 1 and key > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and key < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root
    
    def preorder_traversal(self, node):
        if node is None:
            return []
        result = [node.data]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

def preorder_to_avl(preorder):
    if not preorder:
        return []

    avl_tree = AVLTree()
    avl_tree.insert(preorder[0])

    for i in range(1, len(preorder)):
        avl_tree.insert(preorder[i])

    return avl_tree.preorder_traversal(avl_tree.root)

def dot_avl(preorder):
    if not preorder:
        return None

    avl_tree = AVLTree()
    avl_tree.insert(preorder[0])

    for i in range(1, len(preorder)):
        avl_tree.insert(preorder[i])

    # Generar el archivo .dot correspondiente al árbol AVL generado
    graph = ''
    stack = [avl_tree.root]
    while stack:
        node = stack.pop()
        if node:
            #graph += f'  {node.data} [label="{node.data}"];\n'
            if node.left:
                graph += f'  {node.data} -> {node.left.data};\n'
                stack.append(node.left)
            if node.right:
                graph += f'  {node.data} -> {node.right.data};\n'
                stack.append(node.right)
    
    return graph


class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

#print(preorder_to_avl([3, 2, 1, 5, 4]))