#   Importando el módulo "requests" para usar las API de Binance

import requests

#   Presentación del Programa

print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("Programa que solicita tres Cipto Monedas y Valida que sean validas de acuerdo a la Base de Datos")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Las únicas Cripto Monedas soportadas en este programa son: BTC, BCC, LTC, ETH, ETC y XRP")
print("Este programa solo será 100% útil si has instalado en tu S.O el módulo requests desde la consola de Comando o Terminal con los comandos:")
print("Windows: pip install requests - - - MacOS: pip3 install requests")
print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Definición de las Cripto Monedas Válidas

Criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]

#   API REST de Binance para BitCoin: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
#   API REST de Binance para BCC: https://api.binance.com/api/v3/ticker/price?symbol=BCCUSDT
#   API REST de Binance para LTC: https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT
#   API REST de Binance para ETH: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
#   API REST de Binance para ETC: https://api.binance.com/api/v3/ticker/price?symbol=ETCUSDT
#   API REST de Binance para XRP: https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT

#   Definiendo la función para usar la API de Binance y obtener el valor de la Cripto Moneda contenida en la lista "Criptos"

def valorMoneda(moneda):
    
    """Esta función detecta el valor actual de la Cripto Moneda de acuerdo al día con la API : Binance"""

    #   Referencia usada del programa de Prueba: Prueba_TomaDatosAPI.py el cual también desarrolle
    
    cripto = requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+moneda+"USDT").json()
    coin = float(cripto['price'])
    return coin

#   Definiendo la función para tomar los nombres de las Cripto Monedas

def criptoMoneda(c1,c2,c3):
    
    """Función para realizar los cálculos de las Cripto Monedas"""

    #   Verificando que las Cripto Monedas ingresadas sean válidas

    while ( c1 and c2 and c3 ) not in Criptos:

        print("Cripto Moneda no válida, por favor inténtalo de nuevo")
        c1 = str(input("Por favor ingrese el nombre de la Cipto Moneda 1:"))
        c2 = str(input("Por favor ingrese el nombre de la Cipto Moneda 2:"))
        c3 = str(input("Por favor ingrese el nombre de la Cipto Moneda 3:"))
    
    #   Despues de verificadas las monedas, se solicitan cantidades.

    else:
        
        cant1=float(input("Por favor ingrese la cantidad para la Cripto Moneda {}: ".format(c1)))
        cant2=float(input("Por favor ingrese la cantidad para la Cripto Moneda {}: ".format(c2)))
        cant3=float(input("Por favor ingrese la cantidad para la Cripto Moneda {}: ".format(c3)))

        #   Haciendo tiempo y realizando los cálculos correspondientes
        
        print("Haciendo cálculos...")
        print(".......")
    
    #   Asignamos cotizaciones de las CriptoMonedas al día de hoy con la API de Binance

    crip1 = valorMoneda(c1)
    crip2 = valorMoneda(c2)
    crip3 = valorMoneda(c3)
    
    canT1=cant1*crip1
    canT2=cant2*crip2
    canT3=cant3*crip3
    canT=canT1+canT2+canT3

    #   Retornando resultados

    return canT,canT1,canT2,canT3,c1,c2,c3

#   Inicio Lógico del Programa
#   Petición del nombre de las Cripto Monedas

Cripto1 = str(input("Por favor ingrese el nombre de la Cipto Moneda 1:"))
Cripto2 = str(input("Por favor ingrese el nombre de la Cipto Moneda 2:"))
Cripto3 = str(input("Por favor ingrese el nombre de la Cipto Moneda 3:"))

#   Asignado DINÁMICAMENTE los valor de "canT,canT1,canT2 y canT3" de la función "criptoMoneda" a las variables "can,can1,can2 y can3"
#   Adicionalmente se vuelven a asignar las variales "Cripto1,Cripto2 y Cripto3" pues puede que los valores cambien en la función "criptoMoneda"

can,can1,can2,can3,Cripto1,Cripto2,Cripto3 = criptoMoneda(Cripto1,Cripto2,Cripto3)

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