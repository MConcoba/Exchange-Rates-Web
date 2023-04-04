from models.general_node import GeneralNodo


class Data(GeneralNodo):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.id = data['id']
        self.date = data['date']
        self.iso = data['iso']
        self.country = data['country']
        self.value = data['value']
