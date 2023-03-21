
from io import open
#from proyectoUpateco import*


class Recetas():

    def __init__(self, receta):

    #     self.nombre = nombre
    #     self.ingredientes = ingredientes
    #     self.preparacion = preparacion
    #     self.tiempoElaboracion = tiempoElaboracion
    #     self.fecha = fecha
        self.receta = []

    def agregar_receta(self, receta):
        # self.receta.append(receta)
        receta = open("nombre2.txt", "w")  # creacion del plato de la receta
        # (un boton)que agregue = cuadroTexto linea 24
        receta.write("linea16assdasd")
        receta.close()
        # agregar_receta.close()

    def modificar_receta(self):
        #if boton modificar_receta (receta) video 37 
        # llama a receta.txt =open("receta.txt","a")
        #receta.txt.write("\n")

        pass

    def eliminar_receta(self):

        pass

    def receta_aleatoria(self):
        pass
    
plato1=Recetas("papas")
plato1.agregar_receta("asd")

