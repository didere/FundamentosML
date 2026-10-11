import pandas as pd
from sklearn.linear_model import LogisticRegression

# --- Carga de datos ---------------------------------------------------------
df = pd.read_csv("Entrenamiento_v.csv", encoding="utf-8-sig")

atributos = ["Intensidad_Accion", "Complejidad_Historia", "Necesidad_Estrategia",
             "Habilidad_Requerida", "Competitividad"]
columna_clase = "Genero_Videojuego"

clases_unicas = df[columna_clase].str.strip().unique()
sub_dataframes, modelos = {}, {}

# --- Un modelo "clase vs. resto" (uno contra todos) por cada género ----------
for clase in clases_unicas:
    sub_df = df.copy()
    sub_df[columna_clase] = sub_df[columna_clase].apply(
        lambda x: "si" if str(x).strip() == clase else "no")
    sub_dataframes[clase] = sub_df

    X = sub_df[atributos].values
    y = (sub_df[columna_clase] == "si").astype(int).values   # si=1, no=0

    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X, y)
    modelos[clase] = modelo

# --- Casos de prueba: se leen desde Prueba_v.csv ----------------------------
prueba = pd.read_csv("Prueba_v.csv", encoding="utf-8-sig")
nuevos = prueba[atributos].copy()
clase_real = prueba[columna_clase].str.strip()

# --- Predicción: gana el modelo con mayor probabilidad de "si" ---------------
probabilidades = pd.DataFrame(
    {c: m.predict_proba(nuevos[atributos].values)[:, 1] for c, m in modelos.items()})
nuevos["Genero_predicho"] = probabilidades.idxmax(axis=1)
nuevos["Genero_real"] = clase_real
nuevos["Acerto"] = nuevos["Genero_predicho"] == nuevos["Genero_real"]

# --- Resultados por modelo ---------------------------------------------------
for clase, modelo in modelos.items():
    proba = modelo.predict_proba(nuevos[atributos].values)  # [P(no), P(si)]

    print("=" * 50)
    print(f"SUB-DATAFRAME: {clase} vs. resto")
    print("=" * 50)
    print("Intercepto:", modelo.intercept_[0])

    print("Coeficientes:")
    for nombre, coef in zip(atributos, modelo.coef_[0]):
        print(f"   {nombre}: {coef:.4f}")

    print("Probabilidades por videojuego nuevo:")
    for i, (p_no, p_si) in enumerate(proba):
        print(f"   Videojuego {i}: P(no) = {p_no:.4f} | P(si) = {p_si:.4f}")
    print()

print("=" * 50)
print("PREDICCIÓN FINAL")
print("=" * 50)
print(nuevos.to_string())
print(f"\nAciertos: {nuevos['Acerto'].sum()} de {len(nuevos)}")
print(f"Precisión: {nuevos['Acerto'].mean():.2%}")