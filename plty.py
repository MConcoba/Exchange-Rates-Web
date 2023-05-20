import tkinter as tk
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.tools import mpl_to_plotly

# Creamos una figura de Plotly
fig = make_subplots(rows=1, cols=1)
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 3, 5]
fig.add_trace(go.Scatter(x=x, y=y, name='linea'), row=1, col=1)

# Convertimos la figura a un objeto tkinter
plotly_fig = mpl_to_plotly(fig)
plotly_widget = go.FigureWidget(plotly_fig)
plotly_widget.update_layout(width=500, height=500)

# Creamos una ventana de tkinter y un marco para el gráfico
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Insertamos el gráfico en el marco
plotly_widget.to_tk().pack(expand=True, fill='both')

# Iniciamos el loop de tkinter
root.mainloop()
