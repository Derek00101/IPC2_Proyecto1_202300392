import graphviz
import os

def graficar_matriz(estaciones, sensores, matriz, titulo, nombre_archivo="grafica"):
    """
    Genera una gráfica con Graphviz para cualquier matriz y la guarda como PNG en la carpeta del proyecto.
    """
    try:
        dot = graphviz.Digraph(comment=titulo, format="png")

        # Nodo central del título
        dot.node("titulo", titulo, shape="box", style="filled", color="lightblue")

        # Crear nodos de estaciones
        for est in estaciones:
            dot.node(est, est, shape="ellipse", color="green")
            dot.edge("titulo", est)

        # Crear nodos de sensores
        for sens in sensores:
            dot.node(sens, sens, shape="box", color="orange")

        # Crear aristas con valores de la matriz
        for i, est in enumerate(estaciones):
            for j, sens in enumerate(sensores):
                if matriz[i][j] != 0:
                    dot.edge(est, sens, label=str(matriz[i][j]))

        # Guardar gráfico en la carpeta del proyecto
        salida = dot.render(nombre_archivo, cleanup=True)
        ruta_absoluta = os.path.abspath(salida)
        print(f" Gráfica generada en: {ruta_absoluta}")

    except Exception as e:
        print(f" Error al generar gráfica: {e}")
