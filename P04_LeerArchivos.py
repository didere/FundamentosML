import pandas as pd
import numpy as np

# Cargar el dataframe
archivo = pd.read_csv("Juegos.csv")

print(archivo)

# Devuelve el nombre de las columnas del dataframe
columns = archivo.columns
print("Columnas del dataframe:")
print(columns)

print("\nDatos de la columna Pico de jugadores Steam:")
df_jugadores = archivo["Pico de jugadores Steam"]
print(df_jugadores)

print("\nMenor número de jugadores en pico:")
print(min(df_jugadores))

print("\nMayor número de jugadores en pico:")
print(max(df_jugadores))

print("\nPromedio de jugadores en pico:")
print(np.mean(df_jugadores))

print("\nDesviación estándar de los jugadores en pico:")
print(np.std(df_jugadores))