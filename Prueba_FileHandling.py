path = "D:\Airtech Communications\Personal\Python\Files"    #   Ruta del Archivo
file = "\Prueba.txt"                                        #   Nombre del Archivo
archivo = path + file                                       #   Dirección completa del archivo
print(archivo)                                              #   Mostrando en pantalla que si se tiene bien la dirección
a = open(archivo,"r")                                       #   "a" contiene el archivo y se solicitó permisos de lectura ("r")
print(a.read())                                             #   Se imprime el archivo que etá contenido en "a"
a.close()                                                   #   Se cierra el archivo
#   También escribiremos en el archivo nueva información con la opción append -> "a" (anexar o añadir)
a = open(archivo, "a")
a.write("\nNueva información")                              #   Cambiamos de línea e ingresamos nuevos datos
a.close()                                                   #   Se cierra el archivo
a = open(archivo, "r")
a.seek(0)                                                   #   Se retorna el cursor dentro del archivo a cero (0)
print(a.read())
a.close()                                                   #   Se cierra el archivo

#   Prueba de ingresar Listos / Diccionarios en el Archivo

lista = [1, 2, 3, 4, 5]
a = open(archivo, "a")
puntero = a.tell()                                          #   Tell() nos retorna la posición del puntero
a.seek(puntero+2)
a.write(str(lista))
a.close()
a = open(archivo, "r")
a.seek(0)
print(a.read())
a.close()

#   Ahora intentaremos pasar un diccionarios
diccionario = {"Daniel":7,"Leidy":3}
print(diccionario)
a = open(archivo, "a")
a.writelines(diccionario)
a.close()
a = open(archivo, "r")
a.seek(0)
print(a.readlines())
a.close()

#   Interactuando con un archivo CSV - Video Tutorial:
#   https://www.youtube.com/watch?v=wmNsecoZ_Go
#   https://www.youtube.com/watch?v=G1SPKDRXbKU

import csv

ar = open("Datos.csv", "w", newline='')
escribir = csv.writer(ar, delimiter=',')
for info in diccionario:
    escribir.writerow(info)
ar.close()

#   En el archivo anterior nos genera un archivo CSV con solo las "key" del diccionario y con los cada letra separado
#   por comas, lo cual no es lo que queremos, intentaremos pasar una lista para ver si obtenemos el resultado esperado

test = [
    "Daniel", 7, 
    "Leidy", 3
]

arc = open("NewDatos.csv", "w", newline='')
write = csv.writer(arc, delimiter = ';')
write.writerow(test)
arc.close()

#   Intentaremos leer el contenido del archivo y mostrarlo en pantalla

arch = open("NewDatos.csv", "r")
read = csv.reader(arch, delimiter = ';')

for row in read:
    user1 = row[0]
    cant1 = row[1]
    user2 = row[2]
    cant2 = row[3]

print(user1, cant1, user2, cant2)