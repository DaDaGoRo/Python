# Declaración de la variable String llamada "Frase"
Frase="Curso de programación en 'Python'"

# Impresión de el primer dígito del String "Frase", en este caso, esperamos la "C" mayuscula de "Curso"
print("Frase[0] =", Frase[0])

# Se ubica el "carro" en la posición 25 del String "Frase" e imprime desde el caracter 26 al 33
print("Frase[25:33] =", Frase[25:33])

# Imprime la longitud de caracteres del String "Frase"
print(int(str.__len__(Frase)))

# Imprime todo el String "Frase"
print(str(Frase))

# Imprime todo el String "Frase" en minusculas completamente
print(str.lower(Frase))

# Imprime todo el String "Frase" en MAYUSCULAS completamente
print(str.upper(Frase))