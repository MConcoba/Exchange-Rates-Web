from general_nodo import GeneralNodo


class Dato(GeneralNodo):
    def __init__(self, data):
        super().__init__()
        self.data = data
