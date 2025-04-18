#Actividad 2 clase 9 Ordenación personalizada con key
#Ordenar una lista de cadenas por longitud
#Dada la siguiente lista de palabras, ordénalas en orden ascendente según la
#longitud de las cadenas.
words =["apple","grape","banana","pineapple","kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)