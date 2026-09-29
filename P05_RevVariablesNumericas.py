import matplotlib.pyplot as plt
import pandas as pandita
import numpy as np

archivo = pandita.read_csv("Juegos.csv")
print(archivo)

#devuelve el nombre de las columnas del dataframe
#columns = archivo.columns
#prints(columns)

columns = ["Año de salida", "Pico de jugadores Steam"]

print("Metricas estadísticas: ")
for col in columns:
    print("Columna analizada: " + col)
    min = archivo[col].min()
    max = archivo[col].max()
    promedio = np.mean(archivo[col])
    desvstd = np.std(archivo[col])
    print("Min: " + str(min))
    print("Max: " + str(max))
    print("Promedio: " + str(promedio))
    print("Desvstd: " + str(desvstd))
    print()

    archivo.boxplot(column=col)
    plt.show()

#df[df["Ciudad"] == "Tampico"]