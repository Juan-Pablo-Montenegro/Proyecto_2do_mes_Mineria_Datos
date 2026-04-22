import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conexion = sqlite3.connect("sistemas_planetarios.db")

consulta_1 = "SELECT discoverymethod, AVG(pl_rade) FROM planetas GROUP BY discoverymethod;"
consulta_2 = "SELECT * FROM planetas;"

df_1 = pd.read_sql_query(consulta_1, conexion)
df_2 = pd.read_sql_query(consulta_2, conexion)

conexion.close()

print("")
print("Radio promedio de planetas agrupado por el metodo de descubrimiento")
print("")
print(df_1)

# Falta quitar los datos repetidos

mascara = (df_2["pl_rade"] < 2.5) & (df_2["pl_eqt"] > 200) & (df_2["pl_eqt"] < 320)
df_habitabilidad = df_2[mascara]

plt.scatter(df_2["st_teff"], df_2["pl_eqt"], s=5, c="gray")
plt.scatter(df_habitabilidad["st_teff"], df_habitabilidad["pl_eqt"], s=5, c="blue")

plt.xlabel("Temperatura de la estrella [K]")
plt.ylabel("Temperatura de equilibrio del planeta [K]")
plt.title("Gráfica 1")

plt.show()
