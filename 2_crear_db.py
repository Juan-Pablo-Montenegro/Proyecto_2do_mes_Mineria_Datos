import pandas as pd
import sqlite3

df = pd.read_csv("exoplanetas_bruto.csv")
print(f"Hay un total de {len(df)} planetas en el archivo exoplanetas_bruto.csv")
print("Vamos a crear la base de datos SQL")

conexion = sqlite3.connect("sistemas_planetarios.db")
#cursor = conexion.cursor()

df.to_sql('planetas', conexion, if_exists='replace', index=False)

conexion.close()

print("")
print("Fin del programa")
