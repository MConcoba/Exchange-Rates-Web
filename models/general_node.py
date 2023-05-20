class GeneralNodo():

    def __init__(self, data, parent=None, is_root=False, is_left=False, is_right=False):
        self.next = None
        self.prev = None
        self.left = None
        self.right = None
        self.data = data
        self.id = data['id']
        self.parent = parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right
        self.height = 1
        

class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class NodeHash:

    def __init__(self, id, datos) -> None:
        self.id = id,
        self.datos = datos