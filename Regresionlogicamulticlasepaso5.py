import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Entrenamiento.csv", encoding="utf-8-sig")

atributos = ["velocidad_max", "aceleracion", "capacidad_carga",
             "eficiencia_combustible", "seguridad"]

clases_unicas = df["Clase"].str.strip().unique()
sub_dataframes, modelos = {}, {}

for clase in clases_unicas:
    sub_df = df.copy()
    sub_df["Clase"] = sub_df["Clase"].apply(lambda x: "si" if str(x).strip() == clase else "no")
    sub_dataframes[clase] = sub_df

    X = sub_df[atributos].values
    y = (sub_df["Clase"] == "si").astype(int).values   # si=1, no=0

    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X, y)
    modelos[clase] = modelo
    # ... imprime intercepto y coeficientes por atributo
nuevos = pd.DataFrame(
    [
        [95, 90, 15, 35, 65],
        [60, 50, 85, 55, 90],
        [72, 62, 40, 80, 78],
        [50, 40, 95, 45, 82],
    ],
    columns=atributos,
)
# Predicción: probabilidad de "si" de cada modelo -> gana la mayor
probabilidades = pd.DataFrame({c: m.predict_proba(nuevos.values)[:, 1] for c, m in modelos.items()})
nuevos["Clase_predicha"] = probabilidades.idxmax(axis=1)

for clase, modelo in modelos.items():
    # predict_proba devuelve dos columnas: [P(no), P(si)]
    proba = modelo.predict_proba(nuevos[atributos].values)

    print("=" * 50)
    print(f"SUB-DATAFRAME: {clase} vs. resto")
    print("=" * 50)

    print("Intercepto:", modelo.intercept_[0])

    print("Coeficientes:")
    for nombre, coef in zip(atributos, modelo.coef_[0]):
        print(f"   {nombre}: {coef:.4f}")

    print("Probabilidades por vehículo nuevo:")
    for i, (p_no, p_si) in enumerate(proba):
        print(f"   Vehículo {i}: P(no) = {p_no:.4f} | P(si) = {p_si:.4f}")
    print()