from listas.listas_frecuencias import ListaFrecuencias

class SensorSuelo:
    def __init__(self, id_sensor, nombre):
        self.id = id_sensor
        self.nombre = nombre
        self.frecuencias = ListaFrecuencias()
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
