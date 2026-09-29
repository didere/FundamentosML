import pandas as pd
df=pd.read_csv("Juegos.csv")

#num
if df["Año de salida"].max() != df["Año de salida"].min():
 df["Año_norm"] = (df["Año de salida"] - df["Año de salida"].min()) / (
    df["Año de salida"].max() - df["Año de salida"].min()
)
if df["Pico de jugadores Steam"].max() != df["Pico de jugadores Steam"].min():
 df["Peak-norm"] = (df["Pico de jugadores Steam"] - df["Pico de jugadores Steam"].min()) / (
    df["Pico de jugadores Steam"].max() - df["Pico de jugadores Steam"].min()
)

 df["EmpNorm"] = (
     df["Empresa desarrolladora"]
     .astype(str)
     .str.lower()
     .str.strip()
     .str.replace("[áàäâ]", "a", regex=True)
     .str.replace("[éèëê]", "e", regex=True)
     .str.replace("[íìïî]", "i", regex=True)
     .str.replace("[óòöô]", "o", regex=True)
     .str.replace("[úùüû]", "u", regex=True)
     .str.replace("[^a-z0-9 ]", "", regex=True)
 )

df["Año estandarizado"] = (
    df["Año de salida"] - df["Año de salida"].mean()
) / df["Año de salida"].std()
df["Peak estandarizado"] = (
    df["Pico de jugadores Steam"] - df["Pico de jugadores Steam"].mean()
) / df["Pico de jugadores Steam"].std()

df.to_csv("datos_normalizados.csv", index=False)

