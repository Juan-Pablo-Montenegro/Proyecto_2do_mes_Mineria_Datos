import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conexion = sqlite3.connect("sistemas_planetarios.db")

tabla_limpia = "WITH planetas_no_repetidos AS (SELECT pl_name, discoverymethod, disc_facility, AVG(pl_rade) AS radio_pl, AVG(pl_eqt) AS teq_pl, AVG(st_teff) AS tef_es FROM planetas GROUP BY pl_name) " # Quitamos los planetas repetidos promediando las mediciones realizadas
consulta_1 = tabla_limpia + "SELECT discoverymethod, AVG(radio_pl) FROM planetas_no_repetidos GROUP BY discoverymethod;"
consulta_2 = tabla_limpia + "SELECT * FROM planetas_no_repetidos;"

df_1 = pd.read_sql_query(consulta_1, conexion)
df_2 = pd.read_sql_query(consulta_2, conexion)

conexion.close()

print("")
print("Radio promedio de planetas agrupado por el metodo de descubrimiento")
print("")
print(df_1)

mascara = (df_2["radio_pl"] < 2.5) & (df_2["teq_pl"] > 200) & (df_2["teq_pl"] < 320)
df_habitabilidad = df_2[mascara]

plt.figure(figsize=(14, 8))

plt.scatter(df_2["tef_es"], df_2["teq_pl"], s=5, c="gray")
plt.scatter(df_habitabilidad["tef_es"], df_habitabilidad["teq_pl"], s=5, c="blue")

plt.xlabel("Temperatura de la estrella [K]")
plt.ylabel("Temperatura de equilibrio del planeta [K]")
plt.title("Gráfica 1")

plt.legend(["Todos los planetas no repetidos", "Planetas potencialmente habitables"],)

plt.show()
