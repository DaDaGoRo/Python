print("Hola Mundo")
var = ["Hola Mundo", "X", "Y"]
exit = "Finalizar"
temp = ""
while temp != exit:
    temp = str(input("Escribe algo: "))
    if temp in var:
        print("Lo que escribiste: {} está en la lista".format(temp))
        posicion = var.index(temp)
        print("Adicionalmente, está en la posición: {}".format(posicion))
    else:
        print("Escribiste un dato que NO está en nuestra base de datos")
else:
    print("Has escrito Finalizar, por lo tanto hemos terminado por ahora")
    print("Fin del programa")
    print(var)
    clase = type(var)
    print(clase)