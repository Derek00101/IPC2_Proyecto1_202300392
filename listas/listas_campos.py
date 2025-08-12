from listas.nodo import Nodo

class ListaCampos:
    def __init__(self):
        self.primero = None
    
    def insertar(self, campo):
        nuevo = Nodo(campo)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)  # luego puedes formatear la salida
            actual = actual.siguiente
