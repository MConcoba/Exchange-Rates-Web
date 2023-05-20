class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

        
class AVLTree:
    
    def insert(self, root, key):
        # Paso 1: inserción normal de un árbol binario
       # self.tooltip(key)
        if not root:
            return NodeAVL(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        # Paso 2: actualizar la altura del nodo padre
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Paso 3: obtener el factor de equilibrio del nodo padre
        balance = self.get_balance(root)
        
        # Paso 4: si el nodo no está balanceado, hacer las rotaciones necesarias
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def tooltip(self, datos):
        formatted_data = "\n".join([f"{key}: {value}" for key, value in datos.items()])
        t = f'{datos["id"]} [tooltip="{formatted_data}"];\n'
       # print(t)
        return t
    
    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        
        y.left = z
        z.right = t2
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def right_rotate(self, z):
        y = z.left
        t3 = y.right
        
        y.right = z
        z.left = t3
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def print_tree(self, root):
        if not root:
            return
        
        #print(root.key, end=" ")
        self.print_tree(root.left)
        self.print_tree(root.right)

    def get_dots(self, root, index, label):
        if not root:
            return ''
        graph = '\n'
        graph += f' label="{label}";\n'
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                """ formatted_data = "\n".join([f"{key}: {value}" for key, value in node.data.items()])
                graph += f'{node.id} [tooltip="{formatted_data}"];\n' """
                graph += f'{index}{node.key} [label = {node.key}];\n'
                if node.left:
                    graph += f'  {index}{node.key} -> {index}{node.left.key};\n'
                    stack.append(node.left)
                if node.right:
                    graph += f'  {index}{node.key} -> {index}{node.right.key};\n'
                    stack.append(node.right)
        #graph += '}'
        return graph




""" avl_tree = AVLTree()
root = None
 
root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)

 
# Imprimir el árbol
avl_tree.print_tree(root)
d = avl_tree.get_dots(root)
print(d)

root = avl_tree.insert(root, 40)
root = avl_tree.insert(root, 50)
root = avl_tree.insert(root, 25)
 """
