class Nodo():

    def __init__(self, id, fecha, moneda, cambio):
        self.id = id
        self.fecha = fecha
        self.moneda = moneda
        self.cambio = cambio
        self.siguiente = None
