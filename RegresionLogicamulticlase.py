import pandas as pd

df = pd.read_csv("Entrenamiento.csv")

# 2. Separar dinámicamente en sub-DataFrames por cada clase
sub_dataframes = {}

for clase in df["Clase"].unique():
    # Filtra las filas donde 'Clase' coincide y resetea el índice
    sub_df = df[df["Clase"] == clase].reset_index(drop=True)
    sub_dataframes[clase] = sub_df

# 3. Acceder a variables individuales si lo prefieres
df_deportivo = sub_dataframes["Deportivo"]
df_suv = sub_dataframes["SUV"]
df_sedan = sub_dataframes["Sedán"]
df_camioneta = sub_dataframes["Camioneta"]

# Ejemplo: Mostrar el sub-dataframe de la clase Deportivo
print("--- Sub-DataFrame: Deportivo ---")
print(df_deportivo.head())