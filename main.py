def mostrar_menu():
    print("Menú principal:")
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
            print("Cargar archivo (por implementar)")
        elif opcion == "2":
            print("Procesar archivo (por implementar)")
        elif opcion == "3":
            print("Escribir archivo salida (por implementar)")
        elif opcion == "4":
            print("Datos del estudiante (por implementar)")
        elif opcion == "5":
            print("Generar gráfica (por implementar)")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
