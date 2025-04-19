import tkinter as tk
from tkinter import ttk
import numpy as np
from Optimo import Optimo
from LRU import LRU
from FifoPlus import FifoPlus
from Fifo import Fifo

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmos de Paginación")
        self.root.minsize(800, 300)  # Tamaño mínimo

        self.setup_ui()

    def setup_ui(self):
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        # Input de procesos
        tk.Label(form_frame, text="Lista de procesos (separados por coma):").grid(row=0, column=0, sticky="w")
        self.entry_process = tk.Entry(form_frame, width=40, justify='center')  # Más estrecho y centrado
        self.entry_process.grid(row=0, column=1, padx=5)

        # Input de número de frames
        tk.Label(form_frame, text="Número de frames:").grid(row=1, column=0, sticky="w")
        self.entry_frames = tk.Entry(form_frame, justify='center')  # Centrado
        self.entry_frames.grid(row=1, column=1, padx=5, pady=5)

        # Selección de algoritmo
        tk.Label(form_frame, text="Seleccione el algoritmo:").grid(row=2, column=0, sticky="w")
        self.algorithm_var = tk.StringVar(value="OPTIMO")
        ttk.Combobox(form_frame, textvariable=self.algorithm_var, values=["OPTIMO", "LRU", "FIFO+", "FIFO"], state="readonly").grid(row=2, column=1, padx=5)

        # Botón de calcular
        tk.Button(form_frame, text="Calcular", command=self.run_algorithm).grid(row=3, column=0, columnspan=2, pady=10)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack()

    def run_algorithm(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        try:
            process_list = list(map(int, self.entry_process.get().split(',')))
            n_frames = int(self.entry_frames.get())
        except ValueError:
            tk.Label(self.table_frame, text="Entrada inválida").pack()
            return

        algoritmo = None
        selected = self.algorithm_var.get()
        if selected == "OPTIMO":
            algoritmo = Optimo(process_list, n_frames)
        elif selected == "LRU":
            algoritmo = LRU(process_list, n_frames)
        elif selected == "FIFO+":
            algoritmo = FifoPlus(process_list, n_frames)
        elif selected == "FIFO":
            algoritmo = Fifo(process_list, n_frames)

        algoritmo.calculate()

        cols = [str(i) for i in range(len(process_list))]
        tree = ttk.Treeview(self.table_frame, columns=cols, show="headings", height=n_frames + 2)
        for col in cols:
            tree.heading(col, text=process_list[int(col)])
            tree.column(col, width=40, anchor='center')

        for i in range(n_frames):
            tree.insert('', 'end', values=algoritmo.table[i])

        tree.insert('', 'end', values=algoritmo.fallos, tags=("fallo",))
        tree.tag_configure("fallo", background="#ffdddd")
        tree.pack()

        # Mostrar la cantidad de fallos fuera de la tabla
        tk.Label(self.table_frame, text=f"Fallos: {algoritmo.falls}", font=("Arial", 10, "bold"), bg="#ddffdd").pack(pady=(5, 0))

       # Actualizar la ventana para que se ajuste al contenido con margen
        self.root.update_idletasks()

        # Obtener el tamaño actual del contenido
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()

        # Añadir un pequeño margen (por ejemplo 20 píxeles en ancho y 30 en alto)
        margin_x = 20
        margin_y = 30
        new_width = max(width + margin_x, 800)
        new_height = max(height + margin_y, 300)

        self.root.geometry(f"{new_width}x{new_height}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
