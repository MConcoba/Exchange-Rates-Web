from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar  import DateEntry
import pandas as pd
import requests
import json
from datetime import timedelta


class Nodo:
     def __init__(self, contador, fecha, moneda, cambio):
        self.contador = contador
        self.fecha = fecha
        self.moneda = moneda
        self.cambio = cambio
        self.siguiente = None
        self.anterior = None


class ListaCircularDoblementeEnlazada:
    
    def __init__(self):
       self.primero = None
       self.ultimo = None
       self.size = 0
       self.contador = 1

    def vacia(self):
        return self.primero == None
     
    def __unir_nodos(self):
        if self.primero !=None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
            self.contador +=1

    def agregar_inicio(self, contador, fecha, moneda, cambio):
        if self.vacia():
            self.primero = self.ultimo = Nodo(self.contador, fecha, moneda, cambio)
            self.contador += 1
        else:
            aux = Nodo(self.contador, fecha, moneda, cambio)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.size += 1
        self.__unir_nodos()


    def agregar_final(self, fecha, moneda, cambio):
        if self.vacia():
           self.primero =self.ultimo = Nodo(id, fecha, moneda, cambio)
        else:
             aux = self.ultimo
             self.ultimo = aux.siguiente = Nodo(id, fecha, moneda, cambio)
             self.ultimo.anterior = aux
        self.__unir_nodos()

    def recorrer_inicio_fin(self):
        aux = self.primero
        datos = []
        while aux:
           todo =  aux.contador, aux.fecha, aux.moneda, aux.cambio
           datos.append(todo)
           aux = aux.siguiente
           if aux == self.primero:
                 break
        return datos 
        
    def recorrer_fin_inicio(self):
        aux = self.ultimo
        while aux:
           print(aux.moneda)
           aux = aux.anterior
           if aux == self.ultimo:
                 break
           
    def buscar(self, cambio): 
         aux = self.primero
         while aux:
             if aux.cambio == cambio:
                 return True
             else:
                 aux =aux.siguiente
                 if aux == self.primero:
                     return False
                 
class ExchangeRatesApp:

    def __init__(self, master):
        self.master = master
        self.contador = 1
        try:
            self.master = master
            ...
        except Exception as e:
            print(e)
        master.title("BIENVENIDOS AL PROYECTO")
        master.geometry("700x550")

        venta_ancho = master.winfo_screenwidth()
        venta_largo = master.winfo_screenheight()

        # Cargar la imange de fondo
        imagen = Image.open("C:\\Users\\sjpc2\\Downloads\\1366_2000.jpeg")
        imagen = imagen.resize((venta_ancho, venta_largo), Image.ANTIALIAS)
        
        self.fondo = ImageTk.PhotoImage(imagen)

        # Crear un canvas
        self.canvas = Canvas(master, width=venta_ancho, height=venta_largo)
        self.canvas.pack(fill="both", expand=True)

        # Mostrar la iamgen
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        self.lb_fecha_i = Label(self.canvas, text="Fecha de Inicio")
        self.lb_fecha_i.place(relx=0.3, rely=0.10, anchor="center")
        
        self.fecha_inicio = DateEntry(
            self.canvas, selectmode='day', year=2022, month=3, day=20, date_pattern='yyyy/mm/dd')
        self.fecha_inicio.place(relx=0.3, rely=0.16, anchor="center")

        self.lb_fecha_f = Label(self.canvas, text="Fecha final")
        self.lb_fecha_f.place(relx=0.7, rely=0.10, anchor="center")
        
        self.fecha_final = DateEntry(
            self.canvas, selectmode='day', year=2022, month=3, day=23, date_pattern='yyyy/mm/dd')
        self.fecha_final.place(relx=0.7, rely=0.16, anchor="center")

        self.button = Button(self.canvas, text="Consultar datos", highlightthickness=0, command=self.validar_fechas)
        self.button.place(relx=0.5, rely=0.25, anchor="center")
        
        self.table = pd.DataFrame(columns=['Id', 'Fecha', 'Moneda', 'Cambio'])
        self.table_view = Text(master, height=20, width=70)
        self.table_view.columnconfigure(0, minsize=33)
        self.table_view.columnconfigure(1, minsize=33)
        self.table_view.columnconfigure(2, minsize=33)
        self.table_view.columnconfigure(3, minsize=33)
        self.table_view.place(relx=0.5, rely=0.6, anchor="center")

     
    def validar_fechas(self):
        fecha_inicio = self.fecha_inicio.get_date()
        fecha_final = self.fecha_final.get_date()

        
        try:
            fecha_inicio = self.fecha_inicio.get_date()
            fecha_final = self.fecha_final.get_date()
            ...
        except Exception as e:
            print(e)

        if fecha_inicio >= fecha_final:
            messagebox.showerror("Error", "Las Fechas No Son Validas")
        else:
            # Fechas a consultar
            dias = []
            # dias = [2023-02-20, 2023-02-25, ]
            actual = fecha_inicio
            while actual <= fecha_final:
                dias.append(actual)
                actual += timedelta(days=1)
            
            # Se instancia la clase de Lista circular doblemente enlazada
            listaCircular = ListaCircularDoblementeEnlazada()
        
            # bucle para obtener los cambios de cada dia
            for d in dias:
                url = "https://api.apilayer.com/exchangerates_data/" + d.strftime('%Y-%m-%d') + "?símbolos=JPY,GTQ&base=USD"
                headers = {"apikey": "M4gbYvkYE2GHZTXAPGqrXhVh9vvJzVdT"}
                response = requests.get(url, headers=headers)
                data = json.loads(response.text)
                
                # Se ingresan los datos a la estructura 
                for moneda, cambio in data['rates'].items():
                    listaCircular.agregar_inicio(self.contador, d.strftime('%Y-%m-%d'), moneda, cambio)

                                
            # Se oculta el mensaje de carga
            #self.loading_label.pack_forget()
        
            # Se consulta la funcion que retoran los datos desde la estrucutra
            for id, fecha, moneda, cambio in listaCircular.recorrer_inicio_fin():
                listaCircular.agregar_inicio(self.contador, fecha, moneda, cambio)
                new_row = {'Id': id, 'Fecha': fecha, 'Moneda': moneda, 'Cambio': cambio}
                self.table = pd.concat([self.table, pd.DataFrame(new_row, index=[0])], ignore_index=True)

                self.contador += 1
            # Se muestra la tabla con datos en la vista
            self.table_view.insert('end', self.table.to_string(index=False))


if __name__ == '__main__':       

    root = Tk()
    app = ExchangeRatesApp(root)
    root.mainloop()
 
class Nodo:
    def __init__(self, id):
        self.id = id
        self.izquierdo = None
        self.derecho = None
 
class Arbol:
    def __init__(self):
        self.raiz = None
 
    def agregar_nodo(self, id):
        if self.raiz is None:
            self.raiz = Nodo(id)
        else:
            self._agregar_nodo(id, self.raiz)
 
    def _agregar_nodo(self, id, nodo_actual):
        if id < nodo_actual.id:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(id)
            else:
                self._agregar_nodo(id, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None: 
                nodo_actual.derecho = Nodo(id)
            else:
                self._agregar_nodo(id, nodo_actual.derecho)
 
    def dibujar_arbol(self, canvas, x, y, nodo_actual):
        if nodo_actual is not None:
            radio = 30
            canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="white")
            canvas.create_text(x, y, text=str(nodo_actual.id))
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
arbol.agregar_nodo(1)


ventana = Tk("arbol binario")
canvas = Canvas(ventana, width=500, height=500)
canvas.pack()
arbol.dibujar_arbol(canvas, 250, 50, arbol.raiz)
ventana.mainloop()