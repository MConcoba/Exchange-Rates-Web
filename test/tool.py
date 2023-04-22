import tkinter as tk
import graphviz as gv
import os
from PIL import Image, ImageDraw, ImageFont

# Función que crea el grafo con Graphviz
def create_graph():
    # Definir el grafo
    dot = gv.Digraph()
    dot.node('1', '1', tooltip='Nodo 1')
    dot.node('2', '2', tooltip='Nodo 2')
    dot.node('3', '3', tooltip='Nodo 3')
    dot.node('4', '4', tooltip='Nodo 4')
    dot.node('5', '5', tooltip='Nodo 5')
    dot.edge('2', '1')
    dot.edge('2', '4')
    dot.edge('4', '3')
    dot.edge('4', '5')

    
    
    # Guardar el archivo temporal en una ubicación fija
    temp_file = os.path.join(os.getcwd(), 'temp')
    dot.render(temp_file, format='png')
    
    # Crear la imagen del grafo con etiquetas
    image = add_labels_to_graph(dot, temp_file)
    
    # Mostrar la imagen en un label
    img_tk = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=img_tk)
    label.image = img_tk
    label.pack()

def add_labels_to_graph(dot, temp_file):
    # Abrir la imagen con PIL
    image = Image.open(temp_file)

    # Obtener el tamaño de la imagen
    width, height = image.size

    # Crear un nuevo objeto de imagen para el cuadro de texto
    text_image = Image.new('RGBA', (width, 100), (255, 255, 255, 255))

    # Crear un objeto de dibujo para el cuadro de texto
    draw = ImageDraw.Draw(text_image)

    # Definir la fuente y el tamaño del texto
    font = ImageFont.truetype('arial.ttf', size=12)

    # Definir la posición del primer nodo
    x = 50
    y = height + 20

    # Iterar sobre los nodos y agregar las etiquetas al cuadro de texto
    for node in dot.nodes():
        tooltip = dot.attr('node', node).get('tooltip')
        if tooltip:
            draw.text((x, y), tooltip, font=font, fill=(0, 0, 0, 255))
            x += 120

    # Unir la imagen del grafo y el cuadro de texto
    image = Image.alpha_composite(image, text_image)

    # Guardar la imagen final
    image.save(temp_file)
    
    return image

# Crear la ventana principal
root = tk.Tk()

# Crear el botón que genera el grafo
button = tk.Button(root, text="Generar Grafo", command=create_graph)
button.pack()

# Iniciar el loop principal de la aplicación
root.mainloop()
