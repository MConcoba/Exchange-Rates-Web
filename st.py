from tkinter import *
 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
 
class Arbol:
    def __init__(self):
        self.raiz = None

    def empy(self):
        return self.raiz == None
 
    def agregar_nodo(self, valor):
        if self.empy():
            self.raiz = Nodo(valor)
        else:
            self._agregar_nodo(valor, self.raiz)
 
    def _agregar_nodo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_nodo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_nodo(valor, nodo_actual.derecho)
 
    def dibujar_arbol(self, canvas, x, y, nodo_actual):
        if nodo_actual is not None:
            radio = 30
            canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="white")
            canvas.create_text(x, y, text=str(nodo_actual.valor))
            if nodo_actual.izquierdo is not None:
                x_izquierdo = x - 100
                y_izquierdo = y + 100
                canvas.create_line(x, y, x_izquierdo, y_izquierdo)
                self.dibujar_arbol(canvas, x_izquierdo, y_izquierdo, nodo_actual.izquierdo)
            if nodo_actual.derecho is not None:
                x_derecho = x + 100
                y_derecho = y + 100
                canvas.create_line(x, y, x_derecho, y_derecho)
                self.dibujar_arbol(canvas, x_derecho, y_derecho, nodo_actual.derecho)
 
arbol = Arbol()
arbol.agregar_nodo(10)
arbol.agregar_nodo(5)
arbol.agregar_nodo(15)
arbol.agregar_nodo(3)
arbol.agregar_nodo(7)

ventana = Tk()
canvas = Canvas(ventana, width=500, height=500)
canvas.pack()
arbol.dibujar_arbol(canvas, 250, 50, arbol.raiz)
ventana.mainloop()