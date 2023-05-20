import pandas as pd
import requests
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import random  # Importar la biblioteca random
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm



class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self._update_height(node)

        balance_factor = self._balance_factor(node)

        if balance_factor > 1:  # Left-heavy
            if key < node.left.key:
                node = self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                node = self._right_rotate(node)
        elif balance_factor < -1:  # Right-heavy
            if key > node.right.key:
                node = self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                node = self._left_rotate(node)

        return node


    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def inorder_traversal(self):
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.data)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result

    def plot_tree(self):
        G = nx.DiGraph()
        pos = {}
        labels = {}
        if self.root is not None:
            self._generate_graph(self.root, G, pos, labels, 0, 0)
            fig, ax = plt.subplots()
            nx.draw(G, pos, labels=labels, with_labels=True, node_size=400, node_color="skyblue", font_size=10,
                    font_weight="bold", ax=ax)
            ax.set_title("Árbol AVL")
            return fig

    def _generate_graph(self, node, G, pos, labels, x, y):
        G.add_node(node)
        labels[node] = node.key
        pos[node] = (x, y)
        if node.left:
            G.add_edge(node, node.left)
            self._generate_graph(node.left, G, pos, labels, x - 2 ** y, y - 1)
        if node.right:
            G.add_edge(node, node.right)
            self._generate_graph(node.right, G, pos, labels, x + 2 ** y, y - 1)


class Node:
    def __init__(self, data=None):
        self.prev = None
        self.next = None
        self.data = data

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.prev = node
            node.next = node
        else:
            tail = self.head.prev
            tail.next = node
            node.prev = tail
            node.next = self.head
            self.head.prev = node

    def traverse(self):
        if self.head is None:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def traverse_reverse(self):
        if self.head is None:
            return
        current = self.head.prev
        while True:
            yield current.data
            current = current.prev
            if current == self.head.prev:
                break

    def update_node(self, index, row_idx, col_idx, new_data):
        if self.head is None:
            return

        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                return

        current.data.iloc[row_idx, col_idx] = new_data


def limpiar_tabla():
    tabla.delete(*tabla.get_children())

class BinarySearchTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if self.data is None:
            self.data = value
            return

        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def inorder_traversal(self):
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.data)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result
from tkinter import messagebox

def on_node_click(event, node_id):
    row = tasas_de_cambio.loc[tasas_de_cambio['ID'] == node_id]
    info = f"ID: {row['ID'].values[0]}\nFecha: {row['Fecha'].values[0]}\nMoneda ISO: {row['Moneda ISO'].values[0]}\nTipo de cambio: {row['Tipo de cambio'].values[0]}"
    messagebox.showinfo("Información de la fila", info)

def on_node_click_avl(event, node):
    row = tasas_de_cambio.loc[tasas_de_cambio['ID'] == node.id]
    info = f"ID: {row['ID'].values[0]}\nFecha: {row['Fecha'].values[0]}\nMoneda ISO: {row['Moneda ISO'].values[0]}\nTipo de cambio: {row['Tipo de cambio'].values[0]}"
    messagebox.showinfo("Información de la fila", info)

def draw_tree(node, canvas, x, y, x_offset, y_offset, radius):
    if node is not None:
        oval = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black', fill='white', tags=f"node{node.data}")
        canvas.create_text(x, y, text=str(node.data), font=("Arial", 12), tags=f"node{node.data}")

        canvas.tag_bind(f"node{node.data}", "<Button-1>", lambda event, node_id=node.data: on_node_click(event, node_id))

        if node.left is not None:
            canvas.create_line(x, y + radius, x - x_offset, y + y_offset, width=2)
            draw_tree(node.left, canvas, x - x_offset, y + y_offset, x_offset, y_offset, radius)

        if node.right is not None:
            canvas.create_line(x, y + radius, x + x_offset, y + y_offset, width=2)
            draw_tree(node.right, canvas, x + x_offset, y + y_offset, x_offset, y_offset, radius)

canvas_width = 3000  # Aumenta el ancho del canvas
canvas_height = 2000  # Aumenta el alto del canvas

x_offset = 1  # Aumenta el desplazamiento horizontal inicial
y_offset = 1  # Aumenta el desplazamiento vertical inicial


def generar_pdf(avl):
    c = canvas.Canvas("balanceo_avl.pdf", pagesize=letter)
    draw_balance(avl.root, c, 10 * cm, 27 * cm, 4 * cm, 2 * cm)
    c.save()
    draw_balance(avl.root, c, 10 * cm, 27 * cm, 4 * cm, 2 * cm, 2*cm)

def draw_balance(node, c, x, y, x_offset, y_offset,radius=15):
    if node is not None:
        balance = AVLTree._balance_factor(node)  # pasar node como argumento
        c.drawString(x, y, f"ID: {node.data}, Balance: {balance}")

        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black', fill='white', tags=f"node{node.data}")
        canvas.create_text(x, y, text=str(node.data), font=("Arial", 12), tags=f"node{node.data}")
        canvas.tag_bind(f"node{node.data}", "<Button-1>", lambda event, node=node: on_node_click_avl(event, node))

        if node.left is not None:
            draw_balance(node.left, c, x - x_offset, y - y_offset, x_offset / 2, y_offset)

        if node.right is not None:
            draw_balance(node.right, c, x + x_offset, y - y_offset, x_offset / 2, y_offset)



    def find(self, node_id):
        node = self.root
        while node is not None:
            if node.node_id == node_id:
                return node
            elif node.node_id > node_id:
                node = node.left
            else:
                node = node.right
        return None






def mostrar_arbol_binario():
    global tasas_de_cambio
    if tasas_de_cambio is None:
        messagebox.showerror("Error", "Por favor, primero obtén las tasas de cambio.")
        return

    ids = tasas_de_cambio['ID'].tolist()
    bst = BinarySearchTree()
    for id_value in ids:
        bst.insert(id_value)

    tree_window = tk.Toplevel(root)
    tree_window.title("Árbol Binario")
    tree_window.geometry("800x600")

    scrollbar_y = tk.Scrollbar(tree_window, orient="vertical")
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x = tk.Scrollbar(tree_window, orient="horizontal")
    scrollbar_x.pack(side="bottom", fill="x")

    canvas = tk.Canvas(tree_window, width=canvas_width, height=canvas_height, bg='white', xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
    canvas.pack()

    scrollbar_x.config(command=canvas.xview)
    scrollbar_y.config(command=canvas.yview)

    canvas.config(scrollregion=(0, 0, canvas_width + x_offset, canvas_height + y_offset))

    draw_tree(bst, canvas, 1000, 90, 90, 80, 20)

dfs = CircularDoubleLinkedList()


def mostrar_arbol_avl():
    global tasas_de_cambio
    if tasas_de_cambio is None:
        messagebox.showerror("Error", "Por favor, primero obtén las tasas de cambio.")
        return

    ids = tasas_de_cambio['ID'].tolist()
    avl = AVLTree()
    for id_value in ids:
        avl.insert(id_value)

    tree_window = tk.Toplevel(root)
    tree_window.title("Árbol AVL")
    tree_window.geometry("800x600")

    fig = avl.plot_tree()
    canvas = FigureCanvasTkAgg(fig, master=tree_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Agregar botón "Imprimir Balanceo"
    imprimir_balanceo_btn = tk.Button(tree_window, text="Imprimir Balanceo", command=lambda: generar_pdf(avl))
    imprimir_balanceo_btn.pack(side=tk.BOTTOM, pady=10)



# Función para obtener las tasas de cambio
def obtener_tasas_de_cambio(fecha_ini, fecha_fin):
    moneda_base = "USD"
    # URL en la API
    url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={fecha_ini}&end_date={fecha_fin}&symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base={moneda_base}"
    payload = {}
    headers= {
        "apikey": "x6J5I3oRy4BjphrilXZO5Iha7qGUDJFD"
    }
    # Solicitud a la API
    response = requests.request("GET", url, headers=headers, data=payload)
    # Procesar respuesta de la API
    status_code = response.status_code
    resultado = response.text
    datos_dic = json.loads(resultado)
    df = pd.DataFrame()
    for date, rates in datos_dic["rates"].items():
        for currency, exchange_rate in rates.items():
            df = pd.concat([df, pd.DataFrame({
                "Fecha": [date],
                "Moneda ISO": [currency],
                "Tipo de cambio": [exchange_rate],
            })], ignore_index=True)
    df.columns = ["Fecha", "Moneda ISO", "Tipo de cambio"]

    # Agregar la columna ID
    df.insert(0, 'ID', range(1, len(df) + 1))

    # Generar números aleatorios únicos
    unique_random_numbers = random.sample(range(1, len(df) + 1), len(df))

    # Asignar los números aleatorios a la columna ID
    df['ID'] = unique_random_numbers

    dfs.append(df)
    result = pd.concat(dfs.traverse(), ignore_index=True)
    return result

# Función para mostrar las tasas de cambio

tasas_de_cambio = None

def mostrar_tasas_de_cambio():
    global tasas_de_cambio
    limpiar_tabla()
    fecha_ini = fecha_inicio.get()
    fecha_fin = fecha_final.get()
    recorrido_seleccionado = tipo_recorrido.get()

    if tasas_de_cambio is None:
        try:
            tasas_de_cambio = obtener_tasas_de_cambio(fecha_ini, fecha_fin)
        except Exception as e:
            mensaje_error.config(text=str(e))
            return

    recorrido = None
    if recorrido_seleccionado == "Normal":
        recorrido = dfs.traverse()
    else:
        recorrido = dfs.traverse_reverse()

    for df in recorrido:
        if recorrido_seleccionado == "Inverso":
            df = df.iloc[::-1]  # Invierte el dataframe si es recorrido inverso
        for index, row in df.iterrows():
            tabla.insert("", "end", values=(row["ID"], row["Fecha"], row["Moneda ISO"], row["Tipo de cambio"]))


# Configuración de la GUI
root = tk.Tk()
root.title("Tasas de Cambio")

formulario = tk.Frame(root)
formulario.pack(padx=20, pady=20)

fecha_inicio_label = tk.Label(formulario, text="Fecha de inicio (AAAA-MM-DD):")
fecha_inicio_label.grid(row=0, column=0, padx=5, pady=5)
fecha_inicio = tk.Entry(formulario)
fecha_inicio.grid(row=0, column=1, padx=5, pady=5)

fecha_final_label = tk.Label(formulario, text="Fecha de fin (AAAA-MM-DD):")
fecha_final_label.grid(row=1, column=0, padx=5, pady=5)
fecha_final = tk.Entry(formulario)
fecha_final.grid(row=1, column=1, padx=5, pady=5)


# Cambia el índice de la fila para "boton_obtener.grid" a "row=3" en lugar de "row=2"

boton_obtener = tk.Button(formulario, text="Obtener tasas de cambio", command=mostrar_tasas_de_cambio)
boton_obtener.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

boton_limpiar = tk.Button(formulario, text="Limpiar tabla", command=limpiar_tabla)
boton_limpiar.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

mensaje_error = tk.Label(formulario, fg="red")
mensaje_error.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

boton_arbol_binario = tk.Button(formulario, text="Árbol Binario", command=mostrar_arbol_binario)
boton_arbol_binario.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

boton_arbol_avl = tk.Button(formulario, text="Árbol AVL", command=mostrar_arbol_avl)
boton_arbol_avl.grid(row=11, column=0, columnspan=2, padx=5, pady=5)


# Después de "fecha_final.grid(row=1, column=1, padx=5, pady=5)"
tipo_recorrido_label = tk.Label(formulario, text="Tipo de recorrido:")
tipo_recorrido_label.grid(row=2, column=0, padx=5, pady=5)
tipo_recorrido = tk.StringVar(formulario)
tipo_recorrido.set("Normal")  # Valor predeterminado
tipo_recorrido_menu = ttk.Combobox(formulario, textvariable=tipo_recorrido, values=["Normal", "Inverso"])
tipo_recorrido_menu.grid(row=2, column=1, padx=5, pady=5)



tabla = ttk.Treeview(root, columns=("ID", "Fecha", "Moneda ISO", "Tipo de cambio"))
tabla.heading("#0", text="")
tabla.heading("ID", text="ID")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Moneda ISO", text="Moneda ISO")
tabla.heading("Tipo de cambio", text="Tipo de cambio")
tabla.pack(padx=20, pady=20)

# Configuración de la GUI (continuación)
tabla.column("#0", width=0)
tabla.column("ID", anchor=tk.CENTER, width=50)
tabla.column("Fecha", anchor=tk.CENTER, width=120)
tabla.column("Moneda ISO", anchor=tk.CENTER, width=120)
tabla.column("Tipo de cambio", anchor=tk.CENTER, width=120)


root.mainloop()