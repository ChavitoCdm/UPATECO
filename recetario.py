class Recetario :
    def __init__(self,nombre,ingredientes,preparacion,tiempoElaboracion,fecha): 
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        self.tiempoElaboracion = tiempoElaboracion
        self.fecha = fecha
        self.receta = []
    def agregarReceta(self,receta):
        self.receta.append(receta)
        
    def modificarReceta(self):
        pass
    def eliminarReceta(self):
        pass
