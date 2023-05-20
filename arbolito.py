import tkinter as tk
import subprocess
from PIL import Image, ImageTk

class ArbolBinario:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.imagen = None


    def insertar(self, valor):
        if self.valor is None:
            self.valor = valor
        elif valor < self.valor:
            if self.izquierda is None:
                self.izquierda = ArbolBinario(valor)
            else:
                self.izquierda.insertar(valor)
        else:
            if self.derecha is None:
                self.derecha = ArbolBinario(valor)
            else:
                self.derecha.insertar(valor)

    def buscar(self, valor):
        if self.valor == valor:
            return self
        elif valor < self.valor and self.izquierda is not None:
            return self.izquierda.buscar(valor)
        elif valor > self.valor and self.derecha is not None:
            return self.derecha.buscar(valor)
        else:
            return None

    def generar_dot(self):
        dot = "digraph G {\n"
        dot += self._generar_dot_recursivo()
        dot += "}\n"
        return dot

    def _generar_dot_recursivo(self):
        dot = ""
        if self.izquierda is not None:
            dot += f"    {self.valor} -> {self.izquierda.valor}\n"
            dot += self.izquierda._generar_dot_recursivo()
        if self.derecha is not None:
            dot += f"    {self.valor} -> {self.derecha.valor}\n"
            dot += self.derecha._generar_dot_recursivo()
        return dot

def crear_imagen_dot(dot, formato="png"):
    proceso = subprocess.Popen(["dot", f"-T{formato}", "-o", f"arbol.{formato}"],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    salida, errores = proceso.communicate(input=dot)
    if proceso.returncode != 0:
        raise subprocess.CalledProcessError(proceso.returncode, "dot", output=errores)
    return f"arbol.{formato}"

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.arbol = ArbolBinario()
        self.arbol.insertar(10)
        self.arbol.insertar(5)
        self.arbol.insertar(15)
        self.arbol.insertar(3)
        self.arbol.insertar(7)
        self.arbol.insertar(12)
        self.arbol.insertar(18)
        self.dibujar()

    def dibujar(self):
        dot = self.arbol.generar_dot()
        imagen = crear_imagen_dot(dot)
        foto = ImageTk.PhotoImage(Image.open(imagen))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=foto)
        
        # Agregar tooltip a cada nodo del árbol
        for valor in [10, 5, 15, 3, 7, 12, 18]:
            nodo = self.arbol.buscar(valor)
            if nodo is not None:
                if nodo.imagen is not None:
                    tooltip_text = f"Valor: {valor}"
                    tooltip = tk.Label(self.canvas, text=tooltip_text, bg="white", relief="solid", borderwidth=1)
                    tooltip.place(x=100+15, y=100+15)
                    nodo.imagen.bind("<Enter>", lambda event, tooltip=tooltip: tooltip.lift())
                    nodo.imagen.bind("<Leave>", lambda event, tooltip=tooltip: tooltip.lower())
                else:
                    print(f"Imagen for node {valor} is None")
            else:
                print(f"Node with value {valor} not found in tree")
                
        self.master.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
