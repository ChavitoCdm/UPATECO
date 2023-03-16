from tkinter import*

raiz = Tk()
raiz.title("Proyecto Upateco 2023 =)")
raiz.config(bg="#6FD6FF")
raiz.geometry("650x650")
marco = Frame(raiz,width=500,height=500)
marco.pack()

miLabel=Label(marco, text="Las Recetas Jodidamente Magicas", fg="red",background="#6FD6FF",justify="center",font=("Comic sans ms" , 20)).pack()

cuadroTexto = Entry(raiz)
cuadroTexto.place(x=150 , y=100)
nombreLabel=Label(raiz,text="Nombre del plato: ").place(x=30 , y=100, )

cuadroTexto2 = Entry(raiz)
cuadroTexto2.place(x=150 , y=120)
ingredienteLabel=Label(raiz,text="Ingredientes ").place(x=30 , y=120)

cuadroTexto3 = Entry(raiz)
cuadroTexto3.place(x=150 , y=140)
ingredienteLabel=Label(raiz,text="tiempo ").place(x=30 , y=140)

tiempoLabel=Label(raiz,text="Recetas agregadas").pack()
#tiempoLabel.place (in=ra)
# 
#  lista de platos que se mostrarian cargados
#######################
listaDePlatos=Listbox(raiz).pack()

raiz.mainloop()

 
