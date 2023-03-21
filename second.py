from tkinter import*

def agregar_receta():
    segunda_ventana = Toplevel()

    segunda_ventana.config(background="pink")
    segunda_ventana.geometry("400x400")
    segunda_ventana.title("Agregando Receta...")
    
    plato=Label(segunda_ventana,text="Nombre de la Receta -> ",height=3).grid(row=0,column=0)
    cuadroPlato = Entry(segunda_ventana).grid(row=0,column=1)

    ingredientes=Label(segunda_ventana,text="Ingredientes -> ",height=3).grid(row=1,column=0)
    cuadroIngredientes = Entry(segunda_ventana).grid(row=1,column=1)

    preparacion=Label(segunda_ventana,text="Preparacion -> ",height=3).grid(row=2,column=0)
    cuadroPreparacion = Entry(segunda_ventana).grid(row=2,column=1)

    tiempo=Label(segunda_ventana,text="Tiempo de preparacion -> ",height=3).grid(row=3,column=0)
    cuadroTiempo = Entry(segunda_ventana).grid(row=3,column=1)

    Agregar = Button(segunda_ventana,text="Agregar Receta",bg="grey",fg="black",width=15 , height= 3,command=agregar_receta).grid(row = 4, column=1 ,padx=5)

# def modificar_receta():
#     segunda_ventana = Toplevel()

#     segunda_ventana.config(background="pink")
#     segunda_ventana.geometry("400x400")
#     segunda_ventana.title("Agregando Receta...")