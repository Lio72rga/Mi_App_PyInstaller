# Definir el diccionario con las palabras y sus significados
diccionario = {
    "almendra": "Fruto del almendro, comestible y muy apreciado.",
    "banana": "Fruto alargado y comestible de la bananera.",
    "cereza": "Fruto del cerezo, redondo y de color rojo.",
    "durazno": "Fruto del duraznero, de piel aterciopelada y pulpa jugosa.",
    "frambuesa": "Fruto comestible del frambueso, de color rojo y sabor agridulce.",
    "guayaba": "Fruto tropical comestible de la guayaba, de piel verde o amarilla.",
    "manzana": "Fruto del manzano, de piel fina y sabor dulce o ácido.",
    "naranja": "Fruto del naranjo, de piel anaranjada y sabor dulce o ácido.",
    "pera": "Fruto del peral, de carne jugosa y sabor dulce.",
    "uva": "Fruto de la vid, redondo y de sabor dulce."
}

# Palabra a buscar
palabra_a_buscar = "naranja"

# Búsqueda en el diccionario
if palabra_a_buscar in diccionario:
    significado = diccionario[palabra_a_buscar]
    print(f'El significado de "{palabra_a_buscar}" es: {significado}')
else:
    print(f'La palabra "{palabra_a_buscar}" no se encuentra en el diccionario.')