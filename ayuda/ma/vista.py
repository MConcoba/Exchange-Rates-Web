import tkinter as tk
import pandas as pd
import random
from Programa2 import obtenercambios

root = tk.Tk()
root.title("Proyecto Programacion 3") # Establecer el titulo ventana principal
root.geometry("700x500")  # Establecer el tamaño de la ventana principal

# Crear un Frame
frame = tk.Frame(root)
frame.pack()

# Crear un Frame para contener el Listbox y el botón
listbox_frame = tk.Frame(frame)
listbox_frame.pack()

# Agregar un Label encima del Listbox
label = tk.Label(listbox_frame, text="Fechas a consultar")
label.pack()

# Crear un Listbox dentro del Frame
listbox = tk.Listbox(listbox_frame, width=20, height=5)
listbox.pack(side=tk.LEFT, padx=30) # Ajustar la posición del Listbox dentro del Frame

days = ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']

# Agregar un botón al lado del Listbox
button = tk.Button(listbox_frame, text="Consultar", command=lambda: actualizar_tabla(obtenercambios(days)))
button.pack(side=tk.LEFT, padx=30) # Ajustar la posición del botón dentro del Fram

# Llenar el Listbox con los valores de la lista 'days'
for day in days:
    listbox.insert(tk.END, day)

# Crear un Frame debajo del Listbox para agregar la tabla
table_frame = tk.Frame(frame, pady=30)
table_frame.columnconfigure(0, weight=1)
table_frame.columnconfigure(1, weight=1)
table_frame.columnconfigure(2, weight=1)
table_frame.pack()

# Se crea la tabla con sus el nombre de las columnas
table = pd.DataFrame(columns=['ID','Fecha', 'Moneda', 'Valor'],index=None)
table_view = tk.Text(table_frame, height=100, width=70) #Agregar el Text en el nuevo Frame
table_view.pack()

def actualizar_tabla(listado):
    global table
    data = []
    for id, fecha, moneda, cambio in listado:
            data.append({'ID':str(id), 'Fecha': fecha, 'Moneda': moneda, 'Valor': cambio})
    pd.set_option("display.max_rows", None)
    
    table = pd.DataFrame(data, columns=['ID', 'Fecha', 'Moneda', 'Valor'],index=None).reindex(columns=['ID', 'Fecha', 'Moneda', 'Valor'],index=None)
    table_view.delete("1.0", tk.END)
    table_view.insert(tk.END, table.to_string(index=False))

root.mainloop()



