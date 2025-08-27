def construir_matriz_suelo(campo):
    estaciones = []
    sensores = []
    
    actual = campo.estaciones.primero
    while actual:
        estaciones.append(actual.dato.id)
        actual = actual.siguiente
    
    actual = campo.sensores_suelo.primero
    while actual:
        sensores.append(actual.dato)
        actual = actual.siguiente
    
    matriz = [[0 for _ in range(len(sensores))] for _ in range(len(estaciones))]
    
    for j, sensor in enumerate(sensores):
        freq = sensor.frecuencias.primero
        while freq:
            est_id = freq.dato.id_estacion
            if est_id in estaciones:
                i = estaciones.index(est_id)
                matriz[i][j] = freq.dato.valor
            freq = freq.siguiente
    
    return estaciones, [s.id for s in sensores], matriz


def construir_matriz_cultivo(campo):
    estaciones = []
    sensores = []
    
    actual = campo.estaciones.primero
    while actual:
        estaciones.append(actual.dato.id)
        actual = actual.siguiente
    
    actual = campo.sensores_cultivo.primero
    while actual:
        sensores.append(actual.dato)
        actual = actual.siguiente
    
    matriz = [[0 for _ in range(len(sensores))] for _ in range(len(estaciones))]
    
    for j, sensor in enumerate(sensores):
        freq = sensor.frecuencias.primero
        while freq:
            est_id = freq.dato.id_estacion
            if est_id in estaciones:
                i = estaciones.index(est_id)
                matriz[i][j] = freq.dato.valor
            freq = freq.siguiente
    
    return estaciones, [s.id for s in sensores], matriz


def mostrar_matriz(estaciones, sensores, matriz, titulo):
    print(f"\n--- {titulo} ---")
    encabezado = "     " + "  ".join(sensores)
    print(encabezado)
    for i, est in enumerate(estaciones):
        fila = [str(matriz[i][j]) for j in range(len(sensores))]
        print(f"{est}: " + "  ".join(fila))


# -------------------
# PATRONES Y AGRUPAMIENTO
# -------------------

def generar_patrones(matriz):
    """Convierte una matriz de frecuencias en una matriz de patrones (0/1)."""
    patrones = []
    for fila in matriz:
        patron = tuple(1 if val > 0 else 0 for val in fila)
        patrones.append(patron)
    return patrones


def agrupar_estaciones(estaciones, patrones, matriz):
    """
    Agrupa estaciones con el mismo patrón.
    Retorna estaciones agrupadas y la matriz reducida.
    """
    grupos = {}
    
    for i, patron in enumerate(patrones):
        if patron not in grupos:
            grupos[patron] = {"estaciones": [], "valores": [0]*len(matriz[0])}
        grupos[patron]["estaciones"].append(estaciones[i])
        
        # Sumar frecuencias de esta estación al grupo
        for j, val in enumerate(matriz[i]):
            grupos[patron]["valores"][j] += val
    
    # Construir resultados
    nuevas_estaciones = []
    nueva_matriz = []
    for datos in grupos.values():
        nombre = ", ".join(datos["estaciones"])
        nuevas_estaciones.append(nombre)
        nueva_matriz.append(datos["valores"])
    
    return nuevas_estaciones, nueva_matriz
