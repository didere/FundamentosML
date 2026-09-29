import statistics
import pandas as pd
#esto evita que pandas se salte algunas lineas a la hora de calcular
pd.set_option("display.max_rows", None)
#esto hace que lea el csv generado previament
df = pd.read_csv("datos_ventas.csv")
#Es el caso a comparar con la formula de la distancia euclidiana la cual es distancia es igual a la raiz cuadrada de(x2 - x1) al cuadrado + y2 - y1) al cuadrado caso nuevo es x1 y y1
nuevo_caso = {"Ventas": -4, "Ganancias": 10}
#formula
df["Distancia"] = (
    (df["Ventas"] - nuevo_caso["Ventas"]) ** 2
    + (df["Ganancias"] - nuevo_caso["Ganancias"]) ** 2
) ** 0.5
#Imprime el dataframe completo despues de calcular la distancia
print("RESULTADOS DE LA DISTANCIA EUCLIDIANA EN TODOS LOS REGISTROS")
print(df)
#ordena el dataframe usando la distancia como referencia y lo imprime
df_ordenado = df.sort_values(by="Distancia")

print(
    "\nREGISTROS ORDENADOS DE MENOR A MAYOR DISTANCIA"
)
print(df_ordenado)
#verifica la cantidad de columnas en el dataframe y las eleva a 0.5 lo cual es la equivalente a la raiz cuadrada del numero
N = len(df)
K = int(N**0.5)

k_vecinos = df_ordenado.head(K)
#saca la moda para ver cual es la clase que es mas prevalente
clase_predicha = statistics.mode(k_vecinos["Caso"])

print("\nRESULTADO FINAL")
print(f"Total de registros N: {N}")
print(f"Valor de K: {K}")
print(f"Clase predicha por la Moda: {clase_predicha}")