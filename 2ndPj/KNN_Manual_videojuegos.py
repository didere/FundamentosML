import statistics
import pandas as pd

# evita que pandas se salte filas al imprimir
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

# lee los csv que estan en la misma carpeta que este script
df = pd.read_csv("Entrenamiento_v.csv", encoding="utf-8-sig")
prueba = pd.read_csv("Prueba_v.csv", encoding="utf-8-sig")

atributos = ["Intensidad_Accion", "Complejidad_Historia", "Necesidad_Estrategia",
             "Habilidad_Requerida", "Competitividad"]
columna_clase = "Genero_Videojuego"

# K clasico: parte entera de la raiz cuadrada de N (N = registros de entrenamiento)
N = len(df)
K = int(N ** 0.5)

print(f"Total de registros de entrenamiento N: {N}")
print(f"Valor de K: {K}")
print(f"Casos de prueba: {len(prueba)}")

resultados = []

# se repite el proceso para cada instancia de prueba
for i, caso in prueba.iterrows():
    # 1.- distancia euclidiana del caso nuevo contra todos los registros (5 dimensiones)
    #     d = raiz de la suma de (x_atributo - caso_atributo)^2
    df["Distancia"] = ((df[atributos] - caso[atributos]) ** 2).sum(axis=1) ** 0.5

    # 2.- ordena de menor a mayor distancia (kind="stable": en empate respeta el orden del csv)
    df_ordenado = df.sort_values(by="Distancia", kind="stable")

    # 3.- se queda con los K vecinos mas cercanos
    k_vecinos = df_ordenado.head(K)

    # 4.- la clase predicha es la moda de los K vecinos
    clase_predicha = statistics.mode(k_vecinos[columna_clase])
    clase_real = caso[columna_clase]
    acerto = clase_predicha == clase_real

    print("\n" + "=" * 70)
    print(f"CASO {i + 1}  |  Clase real: {clase_real}")
    print("=" * 70)
    print(k_vecinos[atributos + [columna_clase, "Distancia"]])
    print(f"Votos de los K vecinos: {k_vecinos[columna_clase].value_counts().to_dict()}")
    print(f"Clase predicha por la Moda: {clase_predicha}  ->  {'ACERTO' if acerto else 'NO ACERTO'}")

    resultados.append({
        "Caso": i + 1,
        "Clase_real": clase_real,
        "Clase_predicha": clase_predicha,
        "Acerto": "Acertó" if acerto else "No acertó",
    })

# resumen final de todas las instancias de prueba
df_resultados = pd.DataFrame(resultados)
aciertos = (df_resultados["Acerto"] == "Acertó").sum()

print("\n" + "=" * 70)
print("RESUMEN DE TODAS LAS INSTANCIAS DE PRUEBA")
print("=" * 70)
print(df_resultados.to_string(index=False))
print(f"\nAciertos: {aciertos} de {len(df_resultados)}")
print(f"Precision: {aciertos / len(df_resultados):.2%}")
