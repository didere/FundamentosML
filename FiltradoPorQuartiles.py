import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("Juegos.csv")


df_jugadores = df["Pico de jugadores Steam"]


Q1 = df_jugadores.quantile(0.25)
Q3 = df_jugadores.quantile(0.75)
IQR = Q3 - Q1

li = Q1 - 1.5 * IQR
ls = Q3 + 1.5 * IQR

outliers = df[
    (df_jugadores < li) | (df_jugadores > ls)
]

df_limpio = df[
    (df_jugadores >= li) & (df_jugadores <= ls)
]


print(f"Cuartil 1 (Q1): {Q1}")
print(f"Cuartil 3 (Q3): {Q3}")
print(f"IQR: {IQR}")
print(f"Límite inferior: {li}")
print(f"Límite superior: {ls}\n")
print(f"Se encontraron {len(outliers)} outliers:")
print(outliers)