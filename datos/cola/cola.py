## FIFO (Primero en entrear, primero en salir )

class Cola():

    def __init__(self) -> None:
        self.cola = []
        self.size = 0

    def empty(self):
        return len(self.cola) == 0
    
    def push(self, dato):
        self.cola += [dato]
        self.size += 1

    def pop(self):
        if self.empty == True:
            print('La cola esta vacia')
        else:
            self.cola = [self.cola[i] for i in range(1, self.size)]
            self.size -= 1

    def show(self):
        position = self.size - 1
        while position > -1:
            print(f'[{position}]    =>     {self.cola[position]}')
            position -= 1

    def front(self):
        if self.empty == True:
            print('Cola vacia')
        else:
            print(f'Primer dato:  {self.cola[0]}')