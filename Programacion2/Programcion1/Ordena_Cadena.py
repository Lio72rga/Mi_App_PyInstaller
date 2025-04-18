"""Ordenar cadena de caracteres.
Escribe una función llamada ordenar_cadena que tome una cadena
de texto como parámetro y devuelva una nueva cadena con las letras
ordenadas alfabéticamente, manteniendo la distinción entre
mayúsculas y minúsculas. Por ejemplo, si se pasa la cadena
""ProgramacionConPythonEsDivertido"", la función debería devolver "aaCcDdEeghiiimnnnoooooPPrrrsttvy".
"""
def ordenar_cadena(cadena):
    # Ordenar la cadena alfabéticamente manteniendo la distinción entre mayúsculas y minúsculas
    cadena_ordenada = ''.join(sorted(cadena, key=lambda c: (c.lower(), c)))
    return cadena_ordenada

# Ejemplo de uso
cadena = "ProgramacionConPythonEsDivertido"
resultado = ordenar_cadena(cadena)
print(f"La cadena ordenada es: {resultado}")