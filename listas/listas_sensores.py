from listas.nodo import Nodo

class ListaSensores:
    def __init__(self):
        self.primero = None
    
    def insertar(self, sensor):
        nuevo = Nodo(sensor)
        if not self.primero:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente
