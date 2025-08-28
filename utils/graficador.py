import graphviz

def graficar_matriz(estaciones, sensores, matriz, titulo, nombre_archivo="grafica"):
    try:
        dot = graphviz.Digraph(comment=titulo)
        
        # Nodo central del título
        dot.node("titulo", titulo, shape="box", style="filled", color="lightblue")
        
        # Nodos para estaciones
        for est in estaciones:
            dot.node(est, est, shape="ellipse", color="green")
            dot.edge("titulo", est)
        
        # Nodos para sensores
        for sens in sensores:
            dot.node(sens, sens, shape="box", color="orange")
        
        # Relaciones (pesos)
        for i, est in enumerate(estaciones):
            for j, sens in enumerate(sensores):
                if matriz[i][j] > 0:
                    dot.edge(est, sens, label=str(matriz[i][j]))
        
        # Exportar y renderizar
        salida = dot.render(nombre_archivo, format="png", cleanup=True)
        print(f"Gráfica generada: {salida}")
    
    except Exception as e:
        print(f"Error al generar gráfica: {e}")
