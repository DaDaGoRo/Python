#   Presentación del Programa

print("       ")
print("-------       -------")
print("Programa de cálculo de acumulado en Dólares de TRES Cripto Monedas y el valor de cada una de ellas en orden Descendente")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Solicitud del nombre de la primera Cripto Moneda

nombreCriptoMoneda1=str(input("Por favor ingresa el nombre de la Cripto Moneda 1: "))
print("Vale, el nombre de la criptomoneda que ingresaste es: ",nombreCriptoMoneda1)

#   Solicitud de la cantidad acumulada que se tiene de la Cripto Moneda 1

acumuladoCriptoMoneda1=float(input("Por favor ingresa la cantidad acumulada que tienes de esta Cripto Moneda ------> "))
strAcumuladoCM1=str(acumuladoCriptoMoneda1)
print("Vale, has indicado que tienes la cantidad ",strAcumuladoCM1,"de la Cripto Moneda ",nombreCriptoMoneda1)

#   Solicitud del nombre de la segunda Cripto Moneda

nombreCriptoMoneda2=str(input("Por favor ingresa el nombre de la Cripto Moneda 2: "))
print("Vale, el nombre de la criptomoneda que ingresaste es: ",nombreCriptoMoneda2)

#   Solicitud de la cantidad acumulada que se tiene de la Cripto Moneda 2

acumuladoCriptoMoneda2=float(input("Por favor ingresa la cantidad acumulada que tienes de esta Cripto Moneda ------> "))
strAcumuladoCM2=str(acumuladoCriptoMoneda2)
print("Vale, has indicado que tienes la cantidad ",strAcumuladoCM2,"de la Cripto Moneda ",nombreCriptoMoneda2)

#   Solicitud del nombre de la tercera Cripto Moneda

nombreCriptoMoneda3=str(input("Por favor ingresa el nombre de la Cripto Moneda 3: "))
print("Vale, el nombre de la criptomoneda que ingresaste es: ",nombreCriptoMoneda3)

#   Solicitud de la cantidad acumulada que se tiene de la Cripto Moneda 3

acumuladoCriptoMoneda3=float(input("Por favor ingresa la cantidad acumulada que tienes de esta Cripto Moneda ------> "))
strAcumuladoCM3=str(acumuladoCriptoMoneda3)
print("Vale, has indicado que tienes la cantidad ",strAcumuladoCM3,"de la Cripto Moneda ",nombreCriptoMoneda3)

#   Haciendo tiempo y cálculos del orden descendente ... he imprimiendo resultados

print("Haciendo cálculos...")
print(".......")

print("Te presentamos en orden DESCENDENTE la cantidad que tienes de cada Criptomoneda:")

if (acumuladoCriptoMoneda1 > acumuladoCriptoMoneda2 and acumuladoCriptoMoneda1 > acumuladoCriptoMoneda3):
    if (acumuladoCriptoMoneda2 > acumuladoCriptoMoneda3):
        print("La cantidad que más tienes es ",strAcumuladoCM1,"de la Cripto Moneda ",nombreCriptoMoneda1)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda2,"con ",strAcumuladoCM2)
        print("Finalmente, tienes ",strAcumuladoCM3,"de la Cripto Moneda ",nombreCriptoMoneda3)
    else:
        print("La cantidad que más tienes es ",strAcumuladoCM1,"de la Cripto Moneda ",nombreCriptoMoneda1)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda3,"con ",strAcumuladoCM3)
        print("Finalmente, tienes ",strAcumuladoCM2,"de la Cripto Moneda ",nombreCriptoMoneda2)
elif (acumuladoCriptoMoneda2 > acumuladoCriptoMoneda1 and acumuladoCriptoMoneda2 > acumuladoCriptoMoneda3):
    if (acumuladoCriptoMoneda1 > acumuladoCriptoMoneda3):
        print("La cantidad que más tienes es ",strAcumuladoCM2,"de la Cripto Moneda ",nombreCriptoMoneda2)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda1,"con ",strAcumuladoCM1)
        print("Finalmente, tienes ",strAcumuladoCM3,"de la Cripto Moneda ",nombreCriptoMoneda3)
    else:
        print("La cantidad que más tienes es ",strAcumuladoCM2,"de la Cripto Moneda ",nombreCriptoMoneda2)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda3,"con ",strAcumuladoCM3)
        print("Finalmente, tienes ",strAcumuladoCM1,"de la Cripto Moneda ",nombreCriptoMoneda1)
else:
    if (acumuladoCriptoMoneda1 > acumuladoCriptoMoneda2):
        print("La cantidad que más tienes es ",strAcumuladoCM3,"de la Cripto Moneda ",nombreCriptoMoneda3)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda1,"con ",strAcumuladoCM1)
        print("Finalmente, tienes ",strAcumuladoCM2,"de la Cripto Moneda ",nombreCriptoMoneda2)
    else:
        print("La cantidad que más tienes es ",strAcumuladoCM3,"de la Cripto Moneda ",nombreCriptoMoneda3)
        print("Luego de esta, la segunda con mayor cantidad es ",nombreCriptoMoneda2,"con ",strAcumuladoCM2)
        print("Finalmente, tienes ",strAcumuladoCM1,"de la Cripto Moneda ",nombreCriptoMoneda1)

#   Cerrando el programa

print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")