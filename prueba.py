import tkinter as tk

class RecetarioApp:
    def __init__(self, master):
        self.master = master
        self.recetas = []
        
        # Crear widgets
        self.label_nombre = tk.Label(master, text="Nombre:")
        self.entry_nombre = tk.Entry(master)
        self.label_ingredientes = tk.Label(master, text="Ingredientes:")
        self.text_ingredientes = tk.Text(master, height=5)
        self.label_preparacion = tk.Label(master, text="Preparación:")
        self.text_preparacion = tk.Text(master, height=10)
        self.button_agregar = tk.Button(master, text="Agregar", command=self.agregar_receta)
        self.button_eliminar = tk.Button(master, text="Eliminar", command=self.eliminar_receta)
        self.listbox_recetas = tk.Listbox(master)
        
        # Posicionar widgets
        self.label_nombre.grid(row=0, column=0, sticky="W")
        self.entry_nombre.grid(row=0, column=1)
        self.label_ingredientes.grid(row=1, column=0, sticky="W")
        self.text_ingredientes.grid(row=1, column=1)
        self.label_preparacion.grid(row=2, column=0, sticky="W")
        self.text_preparacion.grid(row=2, column=1)
        self.button_agregar.grid(row=3, column=1, sticky="E")
        self.button_eliminar.grid(row=4, column=1, sticky="E")
        self.listbox_recetas.grid(row=5, column=0, columnspan=2)
        
        # Cargar recetas existentes
        self.cargar_recetas()
        
    def agregar_receta(self):
        # Obtener datos de la interfaz
        nombre = self.entry_nombre.get()
        ingredientes = self.text_ingredientes.get("1.0", tk.END).split("\n")
        preparacion = self.text_preparacion.get("1.0", tk.END).split("\n")
        
        # Crear objeto Receta y agregar a la lista de recetas
        receta = Receta(nombre, ingredientes, preparacion)
        self.recetas.append(receta)
        
        # Actualizar interfaz
        self.listbox_recetas.insert(tk.END, nombre)
        
        # Limpiar campos
        self.entry_nombre.delete(0, tk.END)
        self.text_ingredientes.delete("1.0", tk.END)
        self.text_preparacion.delete("1.0", tk.END)
        
    def eliminar_receta(self):
        # Obtener índice de la receta seleccionada en la lista
        seleccion = self.listbox_recetas.curselection()
        if seleccion:
            indice = seleccion[0]
            
            # Eliminar la receta de la lista y de la interfaz
            del self.recetas[indice]
            self.listbox_recetas.delete(indice)
        
    def cargar_recetas(self):
        # Cargar recetas existentes en la lista y en la interfaz
        for receta in self.recetas:
            self.listbox_recetas.insert(tk.END, receta.nombre)


class Receta:
    def __init__(self, nombre, ingredientes, preparacion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.preparacion = preparacion
if __name__ == "__main__":
    # Crear ventana principal y ejecutar el bucle de eventos
    root = tk.Tk()
    app = RecetarioApp(root)
    root.mainloop()


