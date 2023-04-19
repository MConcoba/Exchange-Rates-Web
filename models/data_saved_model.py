from models.general_node import GeneralNodo


class Data(GeneralNodo):
    def __init__(self, data, parent=None, is_root=False, is_left=False, is_right=False):
        super().__init__(parent=parent, is_root=is_root, is_left=is_left, is_right=is_left)
        self.data = data
        self.id = data['id']
        self.date = data['date']
        self.iso = data['iso']
        self.country = data['country']
        self.value = data['value']
       
