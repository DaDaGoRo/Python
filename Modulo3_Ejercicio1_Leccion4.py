#   Presentación del Programa

print("       ")
print("-------       -------")
print("Programa que solicita tres Cipto Monedas y Valida que sean validas de acuerdo a la Base de Datos")
print("las únicas Cripto Monedas soportadas en este programa son: BTC, BCC, LTC, ETH, ETC y XRP")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Definición de las Cripto Monedas Válidas

Criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]

#   Definiendo la función para realizar este programa

def criptoMoneda(c1,c2,c3):
    
    """Función para realizar los cálculos de las Cripto Monedas"""

    #   Verificando que las Cripto Monedas ingresadas sean válidas

    while ( c1 or c2 or c3 ) not  in Criptos:
        print("Cripto Moneda no válida, por favor inténtalo de nuevo")
        c1 = str(input("Por favor ingrese el nombre de la Cipto Moneda 1:"))
        c2 = str(input("Por favor ingrese el nombre de la Cipto Moneda 2:"))
        c3 = str(input("Por favor ingrese el nombre de la Cipto Moneda 3:"))

    #   Despues de verificadas las monedas, se solicitan cantidades y cotizaciones
    else: 
        cant1=float(input("Por favor ingrese la cantidad para la Cripto Moneda 1: "))
        cot1=float(input("Por favor ingrese la cotización para la Cripto Moneda 1: "))
        cant2=float(input("Por favor ingrese la cantidad para la Cripto Moneda 2: "))
        cot2=float(input("Por favor ingrese la cotización para la Cripto Moneda 2: "))
        cant3=float(input("Por favor ingrese la cantidad para la Cripto Moneda 3: "))
        cot3=float(input("Por favor ingrese la cotización para la Cripto Moneda 3: "))

    #   Haciendo tiempo y realizando los cálculos correspondientes

    print("Haciendo cálculos...")
    print(".......")

    canT1=cant1*cot1
    canT2=cant2*cot2
    canT3=cant3*cot3
    canT=canT1+canT2+canT3
    
    #   Retornando resultados

    return canT,canT1,canT2,canT3

#   Petición del nombre de las Cripto Monedas

Cripto1 = str(input("Por favor ingrese el nombre de la Cipto Moneda 1:"))
Cripto2 = str(input("Por favor ingrese el nombre de la Cipto Moneda 2:"))
Cripto3 = str(input("Por favor ingrese el nombre de la Cipto Moneda 3:"))

#   Asignado DINÁMICAMENTE los valor de "canT,canT1,canT2 y canT3" de la función "criptoMoneda" a las variables "can,can1,can2 y can3"

can,can1,can2,can3=criptoMoneda(Cripto1,Cripto2,Cripto3)

#   Imprimiendo Resultados

print("La cantidad de USD que tiene para la Cripto Moneda",Cripto1,"es de",can1)
print("La cantidad de USD que tiene para la Cripto Moneda",Cripto2,"es de",can2)
print("La cantidad de USD que tiene para la Cripto Moneda",Cripto3,"es de",can3)
print("Finalmente, la suma total de USD que tiene en total con sus tres Cripto Monedas es de:",can)

#   Cerrando el programa

print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")