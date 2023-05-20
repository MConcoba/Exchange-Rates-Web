import tkinter as tk
from tkinter import ttk
from datetime import datetime, date, timedelta
import requests
import json
import random

class Node(object):
    def __init__(self, rates, date):
        self.rates = rates
        self.date = date
        self.next = None
        

class CircularList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0

        cur = self.head
        count = 1

        while cur.next != self.head:
            cur = cur.next
            count += 1

        return count

    def add(self, rates, date):
        new_node = Node(rates, date)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head
            self.head = new_node

    def get_data(self):
        data = []
        cur = self.head
        id_counter = 1  #  Inicializa el contador de ID
        while cur.next != self.head:
            for currency, rate in cur.rates.items():
                row = {'id': id_counter, 'fecha': cur.date, 'moneda': currency,
                       'tasa': rate}  #  Incluye el ID en cada fila
                data.append(row)
                id_counter = random.randint(1,500)
            cur = cur.next

        for currency, rate in cur.rates.items():
            row = {'id': id_counter, 'fecha': cur.date, 'moneda': currency,
                   'tasa': rate}  #  Incluye el ID en cada fila
            data.append(row)
            id_counter = random.randint(1,500)

        return data


class NodoBinario:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        # Si el árbol está vacío, creamos el nodo raíz
        if self.raiz is None:
            self.raiz = NodoBinario(valor)
        else:
            # Empezamos a buscar la posición correcta desde la raíz
            nodo_actual = self.raiz
            while True:
                # Si el valor a insertar es menor que el valor del nodo actual, nos movemos hacia la izquierda
                if valor['id'] < nodo_actual.valor['id']:
                    # Si hay un nodo a la izquierda, lo seguimos recorriendo
                    if nodo_actual.izquierda:
                        nodo_actual = nodo_actual.izquierda
                    # Si no hay un nodo a la izquierda, creamos el nuevo nodo aquí
                    else:
                        nodo_actual.izquierda = NodoBinario(valor)
                        nodo_actual.izquierda.padre = nodo_actual
                        break
                # Si el valor a insertar es mayor o igual que el valor del nodo actual, nos movemos hacia la derecha
                else:
                    # Si hay un nodo a la derecha, lo seguimos recorriendo
                    if nodo_actual.derecha:
                        nodo_actual = nodo_actual.derecha
                    # Si no hay un nodo a la derecha, creamos el nuevo nodo aquí
                    else:
                        nodo_actual.derecha = NodoBinario(valor)
                        nodo_actual.derecha.padre = nodo_actual
                        break
    
    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor['id'])
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)
    
    def preorden_traversal(self):
        self.preorden(self.raiz)

class Arbol:
    # Funciones privadas
    def __init__(self, date,nodo, id_counter):
        self.raiz = nodo(id_counter)

    def __agregar_recursivo(self, nodo, date, id_counter):
        if self < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = nodo(id_counter)
            else:
                self.__agregar_recursivo(nodo.izquierda, date, id_counter)
        else:
            if nodo.derecha is None:
                nodo.derecha = nodo(id_counter)
            else:
                self.__agregar_recursivo(nodo.derecha, date, id_counter)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.id_counter, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo, id_counter):
        if nodo is not None:
            print(nodo.id_counter, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo, id_counter):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.id_counter, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.id_counter == busqueda:
            return nodo
        if busqueda < nodo.id_counter:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, date, id_counter):
        self.__agregar_recursivo(self.raiz, date, id_counter)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    

circular_list = CircularList()
def get_exchange_rates(start_date, end_date):
    current_date = end_date
    while current_date >= start_date:
        url = "https://api.apilayer.com/exchangerates_data/" + str(current_date) + \
            "?symbols=JPY,GTQ&base=USD"
        payload = {}
        headers = {
            "apikey": "ZAZmZLHDtfCICekTrFDb2Uo9GO5YS2Hr"
        }
        response = requests.request("GET", url, headers=headers, data=payload, verify=True)


        if response.status_code == 200:
            data = json.loads(response.text)
            rates = {}
            for currency, rate in data['rates'].items():
                rates[currency] = round(rate, 2)
            circular_list.add(rates, str(current_date))

        current_date -= timedelta(days=1)

    return circular_list.get_data()

# Funcion para generar el arbol
def crear_arbol_binario():
    arbol = ArbolBinario()
    for item in circular_list.get_data():
        arbol.insertar(item)
  
    arbol.preorden_traversal()
    return ''
    



#def on_traversal_select(event=None):
    traversal_type = traversal_type_combobox.get()
    # Aquí puedes implementar las diferentes operaciones según el tipo de recorrido seleccionado
    print(f"Tipo de recorrido seleccionado: {traversal_type}")

    def apply_traversal(traversal_type, data):
        # Aquí puedes implementar las diferentes operaciones según el tipo de recorrido seleccionado
        if traversal_type == "Recorrido 1":
            # Aplica la operación de recorrido 1 a la lista 'data'
            data = data[::-1]
        elif traversal_type == "Recorrido 2":
            # Aplica la operación de recorrido 2 a la lista 'data'
            data.sort(key=lambda x: x['moneda'])
        elif traversal_type == "Recorrido 3":
            # Aplica la operación de recorrido 3 a la lista 'data'
            data.sort(key=lambda x: x['tasa'])

        return data

        traversal_type = traversal_type_combobox.get()
        start_date = datetime.strptime(start_date_entry.get(), '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_entry.get(), '%Y-%m-%d').date()

        data = get_exchange_rates(start_date, end_date)  # Obtenemos la lista de datos original
        new_data = apply_traversal(traversal_type, data)  # Aplicamos el recorrido seleccionado

        # Limpiamos la tabla actual
        for item in table.get_children():
            table.delete(item)

        # Llenamos la tabla con los nuevos valores
        for row in new_data:
            table.insert("", "end", values=(row['id'], row['fecha'], row['moneda'], row['tasa']))

#interfaz

def on_submit():
    start_date = datetime.strptime(start_date_entry.get(), '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_entry.get(), '%Y-%m-%d').date()

    data = get_exchange_rates(start_date, end_date)

    for row in data:
        table.insert("", "end", values=(row['id'], row['fecha'], row['moneda'], row['tasa']))

root = tk.Tk()
root.title("Consulta de tipo de cambio")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

start_date_label = ttk.Label(frame, text="Fecha de inicio (YYYY-MM-DD):")
start_date_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
start_date_entry = ttk.Entry(frame)
start_date_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

end_date_label = ttk.Label(frame, text="Fecha de cierre (YYYY-MM-DD):")
end_date_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
end_date_entry = ttk.Entry(frame)
end_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

submit_button = ttk.Button(frame, text="Consultar.", command=on_submit)
submit_button.grid(row=2, columnspan=2, pady=10)

submit_button = ttk.Button(frame, text= "Arbol Binario", command=crear_arbol_binario)
submit_button.grid(row=3, columnspan=3, pady=10)

submit_button = ttk.Button(frame, text="Arbol AVL", command=on_submit)
submit_button.grid(row=4, columnspan=3, pady=10)

#boton recorrido
#traversal_type_label = ttk.Label(frame, text="Tipo de recorrido:")
#traversal_type_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
#traversal_type_combobox = ttk.Combobox(frame, values=["Recorrido 1", "Recorrido 2", "Recorrido 3"])
#traversal_type_combobox.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
#traversal_type_combobox.bind("<<ComboboxSelected>>", on_traversal_select)
#traversal_button = ttk.Button(frame, text="Realizar recorrido", command=lambda: on_traversal_select())

#traversal_button.grid(row=4, columnspan=2, pady=10)

table = ttk.Treeview(root, columns=("ID", "Fecha", "Moneda", "Tipo de cambio"), show="headings")
table.heading("ID", text="ID")
table.heading("Fecha", text="Fecha")
table.heading("Moneda", text="Moneda")
table.heading("Tipo de cambio", text="Tipo de cambio")
table.column("ID", anchor=tk.CENTER, width=50)
table.column("Fecha", anchor=tk.CENTER, width=100)
table.column("Moneda", anchor=tk.CENTER, width=100)
table.column("Tipo de cambio", anchor=tk.CENTER, width=100)
table.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))




scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
scrollbar.grid(row=3, column=1, sticky=(tk.N, tk.S))
table.configure(yscrollcommand=scrollbar.set)



root.columnconfigure(0, weight=1)

root.rowconfigure(3, weight=1)

root.mainloop()