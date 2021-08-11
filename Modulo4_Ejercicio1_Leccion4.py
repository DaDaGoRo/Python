#   Importando el módulo "requests" para usar las API de Binance

import requests

#   Presentación del Programa

print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("Programa que solicita tres Cipto Monedas y Valida que sean validas de acuerdo a la Base de Datos")
print("También, con el nombre ingresado mostrará la abreviación de la Cripto Moneda y su nombre Completo")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Las únicas Cripto Monedas soportadas en este programa son las reales tomadas de la API de Coin-Market")
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

#   Definición de las Cripto Monedas Válidas con la función: valida_cripto()

#   Copiando la API-KEY de la cuenta que creamos.
#   La cuenta está en: https://coinmarketcap.com/api/
#   El usuario es mi correo
#   El password es: Clave123
#   El código de la API se obtiene de: https://pro.coinmarketcap.com/account/
#   Mi clave de API es: 9eae698a-9242-4a25-8769-acd2c4d7a5af

def valida_cripto(coin):

    """Definición de función que valida si el valor ingresado es válido como Cripto Moneda con la API de Coin Market"""

    claveAPI = "9eae698a-9242-4a25-8769-acd2c4d7a5af"
    headers = { #   Esto son los parametros que necesitamos pasar en la peticion para que la API nos pueda devolver la información
        'Accepts':'application/json', #   Esto indica que el formato de la respuesta de la API sera JSON, que es un formato legible en Python
        'X-CMC_PRO_API_KEY' : claveAPI #    Aqui indicamos que usaremos la clave de la API que definimos arriba
        } 

    #   Inicializaremos una lista vacía para ir almacenando en ella, los valores que vamos enontrando más adelante de las CriptoMonedas

    lista_sym = []

    #   Usamos la API con los valores que definimos arriba:

    criptos = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

    #   Para ahora recorreremos el DICCIONARIO que está dentro de otro DICCIONARIO, el cual es "data"
    #   Es decir, recorremos uno-a-uno los valores del diccionario que está dentro de la CLAVE criptos["data"] (el cual es otro diccionario)

    for i in criptos["data"]:   #   Se recorre todo lo contenido en el diccionario "criptos" en su Clave: "data"
        lista_sym.append(i["symbol"])   #   La variable "i" hace el recorrido por todo el diccionario con la clave: symbol

    #   Retornando resultados de la función:

    if coin in lista_sym:   #   Si el valor está en la lista, regrese VERDADERO (True)
        return True
    else:
        return False    #   Sino, regrese FALSO (False)

#   Definición de la función que extrae el nombre completo de la Cripto Moneda

def valida_name (name):

    """Función que obtendrá el Nombre Completo y real de la Cripto Moneda"""

    claveAPI = "9eae698a-9242-4a25-8769-acd2c4d7a5af"
    headers = { #   Esto son los parametros que necesitamos pasar en la peticion para que la API nos pueda devolver la información
        'Accepts':'application/json', #   Esto indica que el formato de la respuesta de la API sera JSON, que es un formato legible en Python
        'X-CMC_PRO_API_KEY' : claveAPI #    Aqui indicamos que usaremos la clave de la API que definimos arriba
        } 

    #   Inicializaremos dos listas vacías para ir almacenando en ellas, los NOMBRES que vamos enontrando más adelante de las CriptoMonedas

    lista_name = []
    lista_sym = []

    #   Usamos la API con los valores que definimos arriba:

    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

    #   Para ahora recorreremos el DICCIONARIO que está dentro de otro DICCIONARIO, el cual es "data"
    #   Es decir, recorremos uno-a-uno los valores del diccionario que está dentro de la CLAVE criptos["data"] (el cual es otro diccionario)

    for i in data["data"]:   #   Se recorre todo lo contenido en el diccionario "data" en su Clave: "data"
        lista_name.append(i["name"])   #   La variable "i" hace el recorrido por todo el diccionario con la clave: name
        lista_sym.append(i["symbol"])   #   La variable "i" hace el recorrido por todo el diccionario con la clave: symbol


    #   Retornando resultados de la función:

    for m in lista_sym: #   Haciendo una iteración con "m" que recorre toda la LISTA llamada "lista_sym"
        if m == name:   #   Ya dentro del for, la variable "m" contiene uno a uno los datos de la lista "lista_sym", por esto se puede Comparar
            indice = lista_sym.index(m) #   Si "m" es igual al nombre ingresado en la función, entonces extrae el índice de donde hubo "match"
            full_name = lista_name[indice]  #   Ese índice se usa para extraer el NOMBRE en la otra lista que contiene ello, llamada "lista_name"

    return full_name    #   Retornamos el nombre completo de la Cripto Moneda

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

    return canT,canT1,canT2,canT3

#   Inicio Lógico del Programa

#   Petición del nombre de las Cripto Monedas y Verificando que las Cripto Monedas ingresadas sean válidas

Cripto1 = str(input("Por favor ingrese el nombre de la Cripto Moneda 1:"))
while not valida_cripto(Cripto1):
    Cripto1= str(input("Moneda inválida, por favor ingrese un nombre válido para la Cipto Moneda 1: "))
print("Verificando la Cripto Moneda ingresada...")
nombre = valida_name(Cripto1)
print("La moneda ingresada es valida")
print("Su nombre completo es {}".format(nombre),"y su símbolo es {}".format(Cripto1))

Cripto2 = str(input("Por favor ingrese el nombre de la Cripto Moneda 2:"))
while not valida_cripto(Cripto2):
    Cripto2= str(input("Moneda inválida, por favor ingrese un nombre válido para la Cipto Moneda 2: "))
print("Verificando la Cripto Moneda ingresada...")
nombre = valida_name(Cripto2)
print("La moneda ingresada es valida")
print("Su nombre completo es {}".format(nombre),"y su símbolo es {}".format(Cripto2))

Cripto3 = str(input("Por favor ingrese el nombre de la Cripto Moneda 3:"))
while not valida_cripto(Cripto3):
    Cripto3= str(input("Moneda inválida, por favor ingrese un nombre válido para la Cipto Moneda 3: "))
print("Verificando la Cripto Moneda ingresada...")
nombre = valida_name(Cripto3)
print("La moneda ingresada es valida")
print("Su nombre completo es {}".format(nombre),"y su símbolo es {}".format(Cripto3))

#   Asignado DINÁMICAMENTE los valor de "canT,canT1,canT2 y canT3" de la función "criptoMoneda" a las variables "can,can1,can2 y can3"

can,can1,can2,can3 = criptoMoneda(Cripto1,Cripto2,Cripto3)

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