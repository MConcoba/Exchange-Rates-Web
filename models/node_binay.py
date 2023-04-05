from models.general_node import GeneralNodo


class BinaryNode(GeneralNodo):
    def __init__(self, data):
        super().__init__()
        self.data = data
