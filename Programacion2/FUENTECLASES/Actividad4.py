#Crea una lista de frutas: Define una lista que contenga nombres de frutas.
# Paso 1: Crear una lista de frutas
frutas = ["manzana", "banana", "naranja", "palta", "uva"]
frutas_info = {
"manzana": {"peso": 150, "color": "rojo"},
"banana": {"peso": 120, "color": "amarillo"},
"naranja": {"peso": 180, "color": "naranja"},
"palta": {"peso": 175, "color": "verde"},
"uva": {"peso": 50, "color": "morado"},
}

# Definir la fruta a clasificar
fruta_clasificar = {"peso": 175, "color": "verde"}  # Cambia los valores para probar diferentes frutas

# Identificar manualmente la fruta correspondiente
fruta_identificada = None
for fruta, info in frutas_info.items():
    if info["peso"] == fruta_clasificar["peso"] and info["color"] == fruta_clasificar["color"]:
        fruta_identificada = fruta
        break

# Imprimir el resultado
if fruta_identificada:
    print(f"La fruta clasificada es: {fruta_identificada}")
else:
    print("No se encontró una fruta que coincida con las características dadas.")