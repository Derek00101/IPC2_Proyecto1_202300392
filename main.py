from listas.listas_campos import ListaCampos
from utils.lector_xml import cargar_xml
from utils.procesador import agrupar_estaciones, construir_matriz_suelo, construir_matriz_cultivo, generar_patrones, mostrar_matriz
from utils.escritor_xml import escritor_xml
from utils.graficador import graficar_matriz



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
            if lista_campos.primero is None:
                print("Debe cargar un archivo primero.")
            else:
                actual = lista_campos.primero
                while actual:
                    campo = actual.dato
                    print(f"\nProcesando campo {campo.id} - {campo.nombre}")
                    
                    # Suelo
                    est, sens, matriz = construir_matriz_suelo(campo)
                    mostrar_matriz(est, sens, matriz, "Matriz F[n,s] (Suelo)")
                    
                    patrones = generar_patrones(matriz)
                    print("\nPatrones Suelo:", patrones)
                    
                    est_reduc, matriz_reduc = agrupar_estaciones(est, patrones, matriz)
                    mostrar_matriz(est_reduc, sens, matriz_reduc, "Matriz Fr[n,s] (Suelo Reducida)")
                    
                    # Cultivo
                    est, sens, matriz = construir_matriz_cultivo(campo)
                    mostrar_matriz(est, sens, matriz, "Matriz F[n,t] (Cultivo)")
                    
                    patrones = generar_patrones(matriz)
                    print("\nPatrones Cultivo:", patrones)
                    
                    est_reduc, matriz_reduc = agrupar_estaciones(est, patrones, matriz)
                    mostrar_matriz(est_reduc, sens, matriz_reduc, "Matriz Fr[n,t] (Cultivo Reducida)")
                    
                    actual = actual.siguiente
        
        elif opcion == "3":
            if lista_campos.primero is None:
                print("Debe cargar y procesar un archivo primero.")
            else:
                ruta = input("Ingrese la ruta y nombre del archivo de salida (ejemplo: salida.xml): ")
                escritor_xml(ruta, lista_campos)

        elif opcion == "4":
            print("\n--- Datos del estudiante ---")
            print("Carné: 202300392")
            print("Nombre: Derek Alessandro Cordova Corado")
            print("Curso: IPC2")
            print("Carrera: Ingeniería en Ciencias y Sistemas")
            print("Semestre: 4to")
            print("Sección: E")
        
        elif opcion == "5":
            if lista_campos.primero is None:
                print("Debe cargar y procesar un archivo primero.")
            else:
                # Mostrar campos disponibles
                print("\nCampos disponibles:")
                actual = lista_campos.primero
                while actual:
                    print(f"- {actual.dato.id}: {actual.dato.nombre}")
                    actual = actual.siguiente
                
                campo_id = input("Ingrese el ID del campo a graficar: ")
                
                # Buscar campo
                actual = lista_campos.primero
                campo = None
                while actual:
                    if actual.dato.id == campo_id:
                        campo = actual.dato
                        break
                    actual = actual.siguiente
                
                if not campo:
                    print("Campo no encontrado.")
                else:
                    print("\nOpciones de gráfica:")
                    print("1. Matriz F[n,s] (Suelo)")
                    print("2. Matriz F[n,t] (Cultivo)")
                    opcion_grafica = input("Seleccione una opción: ")
                    
                    if opcion_grafica == "1":
                        est, sens, matriz = construir_matriz_suelo(campo)
                        graficar_matriz(est, sens, matriz, f"Matriz F[n,s] - {campo.nombre}", "suelo")
                    elif opcion_grafica == "2":
                        est, sens, matriz = construir_matriz_cultivo(campo)
                        graficar_matriz(est, sens, matriz, f"Matriz F[n,t] - {campo.nombre}", "cultivo")
                    else:
                        print("Opción inválida.")
        
        elif opcion == "6":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
