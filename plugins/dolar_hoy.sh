#!/bin/bash

# Obtener la cotización del dólar hoy
cotizacion=$(curl https://www.dolarsi.com/api/api.php?type=valoresprincipales -s | jq '.[0, 1]["casa"] | {nombre, compra, venta}')

# Extraer el valor de compra y venta del dólar de la respuesta JSON
nombre=$(echo "$cotizacion" | jq -r '.nombre' | sed 's/,/./g')
compra=$(echo "$cotizacion" | jq -r '.compra' | sed 's/,/./g')
venta=$(echo "$cotizacion" | jq -r '.venta' | sed 's/,/./g')

# Obtener la fecha y hora actual
fecha=$(date +"%Y-%m-%d %H:%M:%S")

# Verificar si el archivo CSV existe
if [ ! -f ./out/cotizaciones.csv ]; then
  # Si el archivo no existe, crearlo con el encabezado
  echo "Fecha,Nombre,Compra,Venta" > ./out/cotizaciones.csv
fi

echo "Fecha: $fecha"

# Combinar las variables en una cadena con tres columnas
datos=$(paste <(echo "$nombre") <(echo "$compra") <(echo "$venta"))

# Procesar cada fila y separar las tres columnas en tres variables distintas
while IFS=$'\t' read -r n c v; do
  # Imprimir las variables con el formato deseado
  echo "$fecha,$n,$c,$v" >> ./out/cotizaciones.csv
done <<< "$datos"
