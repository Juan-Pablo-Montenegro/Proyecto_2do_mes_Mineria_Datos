#!/bin/bash
echo "Iniciando pipeline astronómico..."

# 1. Definimos la consulta SQL
QUERY="SELECT pl_name, discoverymethod, disc_facility, pl_rade, pl_eqt, st_teff FROM ps WHERE pl_rade IS NOT NULL AND pl_eqt IS NOT NULL"

# 2. Definimos el Endpoint explícito
ENDPOINT="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?format=csv&query="

# 3. Formateamos y descargamos
URL="${ENDPOINT}${QUERY}"
# Reemplazamos los espacios por + para la URL de la NASA Exoplanets Archive
URL_CLEAN=$(echo $URL | sed 's/ /+/g')

wget -q -O exoplanetas_bruto.csv "$URL_CLEAN"
echo "Datos descargados exitosamente."
