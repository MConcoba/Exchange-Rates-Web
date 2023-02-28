from model import Dato


class CircularDouble():

    def __init__(self):
        self.first = None
        self.last = None

    def empy(self):
        return self.first == None

    def add_last(self, data):
        if self.empy():
            self.first = self.last = Dato(data)
        else:
            new = self.last
            self.last = new.next = Dato(data)
            self.last.prev = new
        self.__join_nodes__()

    def __join_nodes__(self):
        if self.first != None:
            self.first.prev = self.last
            self.last.next = self.first

    def show_from_init(self):
        aux = self.first
        while aux:
            print(aux.data)
            aux = aux.next
            if aux == self.first:
                break
