from tkinter import*
from second import*
from modificando import*



def eliminar_receta():
    pass

def receta_aleatoria():
    pass
root = Tk()
root.title("Proyecto Upateco 2023 =)")
root.config(bg="#6FD6FF")

marco = Frame(root,width=500,height=500)
miLabel=Label(root, text="Las Recetas Jodidamente Magicas", fg="red",background="#6FD6FF",justify="center",font=("Comic sans ms" , 20)).grid(row=0 , column=1,padx=50)

#################BOTONES###################################

b1 = Button(root,text="Agregar Receta",bg="grey",fg="black",width=15 , height= 3,command=agregar_receta).grid(row=1, padx=5)
cuadroTexto = Entry(root).grid(row=1 , column=1)

b2 = Button(root,text="Modificar Receta",bg="grey",fg="black",width=15 , height= 3,command=modificar_receta).grid(row=2 , column=0,pady=30)

# b3 = Button(root,text="Eliminar Receta ",bg="grey",fg="black",width=15 , height= 3,command=eliminar_receta).grid(row=3 , column=0)

# b4 = Button(root,text="Receta del dia",bg="grey",fg="black",width=15 , height= 3, command=receta_aleatoria).grid(row=4 , column=0)

#########################################

#nombreLabel=Label(raiz,text="Nombre del plato: ").place(x=30 , y=100, )



#cuadroTexto3 = Entry(raiz)
#cuadroTexto3.place(x=150 , y=140)
#ingredienteLabel=Label(raiz,text="tiempo ").place(x=30 , y=140)

#tiempoLabel=Label(raiz,text="Recetas agregadas").pack()
#tiempoLabel.place (in=ra)
# 
#  lista de platos que se mostrarian cargados
#######################
#listaDePlatos=Listbox(root).pack()
### vamos a crear botones de agregar Receta 
root.mainloop()

 
