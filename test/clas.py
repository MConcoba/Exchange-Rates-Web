class AVLTree:
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.height = 1
            
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return self.Node(value)
            if value < node.value:
                node.left_child = _insert(node.left_child, value)
            else:
                node.right_child = _insert(node.right_child, value)
                
            node.height = 1 + max(self._get_height(node.left_child),
                                  self._get_height(node.right_child))
            
            balance = self._get_balance(node)
            if balance > 1 and value < node.left_child.value:
                return self._rotate_right(node)
            if balance < -1 and value > node.right_child.value:
                return self._rotate_left(node)
            if balance > 1 and value > node.left_child.value:
                node.left_child = self._rotate_left(node.left_child)
                return self._rotate_right(node)
            if balance < -1 and value < node.right_child.value:
                node.right_child = self._rotate_right(node.right_child)
                return self._rotate_left(node)
            
            return node
        
        self.root = _insert(self.root, value)
    
    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node
            elif value < node.value:
                node.left_child = _delete(node.left_child, value)
            elif value > node.value:
                node.right_child = _delete(node.right_child, value)
            else:
                if not node.left_child and not node.right_child:
                    return None
                elif not node.left_child:
                    node = node.right_child
                elif not node.right_child:
                    node = node.left_child
                else:
                    temp_node = self._get_min_node(node.right_child)
                    node.value = temp_node.value
                    node.right_child = _delete(node.right_child, temp_node.value)
                    
            if not node:
                return node
            
            node.height = 1 + max(self._get_height(node.left_child),
                                  self._get_height(node.right_child))
            
            balance = self._get_balance(node)
            if balance > 1 and self._get_balance(node.left_child) >= 0:
                return self._rotate_right(node)
            if balance > 1 and self._get_balance(node.left_child) < 0:
                node.left_child = self._rotate_left(node.left_child)
                return self._rotate_right(node)
            if balance < -1 and self._get_balance(node.right_child) <= 0:
                return self._rotate_left(node)
            if balance < -1 and self._get_balance(node.right_child) > 0:
                node.right_child = self._rotate_right(node.right_child)
                return self._rotate_left(node)
            
            return node
        
        self.root = _delete(self.root, value)
        
    def traverse_in_order(self):
        def _traverse(node):
            if not node:
                return
            _traverse(node.left_child)
            print(node.value)
            _traverse(node.right_child)
            
        _traverse(self.root)
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def _rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node
        
        node.height = 1 + max(self._get_height(node.left_child),
                            self._get_height(node.right_child))
        new_root.height = 1 + max(self._get_height(new_root.left_child),
                                self._get_height(new_root.right_child))
    
        return new_root

    
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left_child) - self._get_height(node.right_child)

