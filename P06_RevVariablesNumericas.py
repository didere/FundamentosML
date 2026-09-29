import matplotlib.pyplot as plt
import pandas as pandita
import numpy as np

archivo = pandita.read_csv("Juegos.csv")

print(archivo)

genero_label = ["Battle Royale", "RPG de acción", "Supervivencia / Acción", "FPS", "MMORPG", "MOBA", "RPG"]

datos = [archivo[archivo["Género"] == g] for g in genero_label]

colums = ["Pico de jugadores Steam"]

for index, genero in enumerate(datos):
    print("Género: " + genero_label[index])
    print("Métricas estadísticas: ")
    for col in colums:
        min_val = genero[col].min()
        max_val = genero[col].max()
        promedio = np.mean(genero[col])
        desvstd = np.std(genero[col])
        print("Columna analizada: " + col)
        print("Min: " + str(min_val))
        print("Max: " + str(max_val))
        print("Promedio: " + str(promedio))
        print("Desvstd: " + str(desvstd))
        print()

        genero.boxplot(column=col)
        plt.title(f"Distribución de {col} en {genero_label[index]}")
        plt.show()