from listas.nodo import Nodo

class ListaFrecuencias:
    def __init__(self):
        self.primero = None
    
    def insertar(self, frecuencia):
        nuevo = Nodo(frecuencia)
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
