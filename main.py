from listas.lista_campos import ListaCampos
from utils.lector_xml import cargar_xml

# Creamos la lista global de campos
lista_campos = ListaCampos()

def mostrar_menu():
    print("\nMenú principal:")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ruta = input("Ingrese la ruta completa del archivo XML: ")
            cargar_xml(ruta, lista_campos)
        
        elif opcion == "2":
            print("Procesar archivo (pendiente)")
        
        elif opcion == "3":
            print("Escribir archivo salida (pendiente)")
        
        elif opcion == "4":
            print("\n--- Datos del estudiante ---")
            print("Carné: 202300392")
            print("Nombre: Derek Alessandro Cordova Corado")
            print("Curso: IPC2")
            print("Carrera: Ingeniería en Ciencias y Sistemas")
            print("Semestre: 4to")
            print("Sección: E")
        
        elif opcion == "5":
            print("Generar gráfica (pendiente)")
        
        elif opcion == "6":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
