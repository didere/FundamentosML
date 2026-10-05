import pandas as pd

# 1. Leer la instancia completa desde el archivo CSV
df = pd.read_csv("Entrenamiento.csv")

# 2. Obtener la lista de clases únicas (ej. Deportivo, SUV, Sedán, Camioneta)
clases_unicas = df["Clase"].unique()

# 3. Crear un diccionario para almacenar un sub-DataFrame por cada clase
sub_dataframes = {}

for clase in clases_unicas:
    # Creamos una copia del DataFrame original
    sub_df = df.copy()

    # Reemplazamos la columna 'Clase': 'si' si coincide con la clase actual, 'no' en caso contrario
    sub_df["Clase"] = sub_df["Clase"].apply(
        lambda x: "si" if str(x).strip() == clase else "no"
    )

    # Guardamos el sub-DataFrame en el diccionario
    sub_dataframes[clase] = sub_df

# ---------------------------------------------------------
# 4. Asignación a variables individuales (opcional)
# ---------------------------------------------------------
# Asumiendo las 4 clases de tu ejemplo:
df_suv = sub_dataframes.get("SUV")
df_deportivo = sub_dataframes.get("Deportivo")
df_sedan = sub_dataframes.get("Sedán")
df_camioneta = sub_dataframes.get("Camioneta")

# ---------------------------------------------------------
# INSTRUCCIONES DE IMPRESIÓN POR SEPARADO
# ---------------------------------------------------------

# Para imprimir el Sub-DataFrame de SUV:
print("=== SUB DATAFRAME: SUV ===")
print(df_suv)

# Para imprimir el Sub-DataFrame de Deportivo:
print("\n=== SUB DATAFRAME: DEPORTIVO ===")
print(df_deportivo)

# Para imprimir el Sub-DataFrame de Sedán:
print("\n=== SUB DATAFRAME: SEDÁN ===")
print(df_sedan)

# Para imprimir el Sub-DataFrame de Camioneta:
print("\n=== SUB DATAFRAME: CAMIONETA ===")
print(df_camioneta)