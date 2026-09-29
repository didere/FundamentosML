import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv("datos_encoding.csv")

print("DATOS ORIGINALES")
print(df)
orden_educativo = {"Secundaria": 0, "Licenciatura": 1, "Doctorado": 2}
df[("nivel_educativo_label")] = df["nivel_educativo"].map(orden_educativo)

print("\nRESULTADO LABEL ENCODING")
print(df[["id", "nivel_educativo", "nivel_educativo_label"]])

df_final = pd.get_dummies(df, columns=["ciudad"], prefix="ciudad", dtype=int)

print("\nDATAFRAME")
print(df_final)