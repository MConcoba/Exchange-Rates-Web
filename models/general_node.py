class GeneralNodo():

    def __init__(self, parent=None, is_root=False, is_left=False, is_right=False):
        self.next = None
        self.prev = None
        self.left = None
        self.right = None
        self.parent = parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right
        
