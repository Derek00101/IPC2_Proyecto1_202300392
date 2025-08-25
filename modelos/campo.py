from listas.listas_estaciones import ListaEstaciones
from listas.listas_sensores import ListaSensores


class Campo:
    def __init__(self, id_campo, nombre):
        self.id = id_campo
        self.nombre = nombre
        self.estaciones = ListaEstaciones()
        self.sensores_suelo = ListaSensores()
        self.sensores_cultivo = ListaSensores()
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
