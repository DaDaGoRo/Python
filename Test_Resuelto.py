"""
Importanto el Módulo "requests", usar las API de CoinMarket.com y Binance.com para:

    1. Solicitar al usuario un código de una Cripto Moneda, luego, conocer si un CÓDIGO de una Cripto Moneda es VALIDA 
       mediante la API de CoinMarket.com

    2. En caso de no ser válida, indicar en pantalla esto y solicitarlo nuevamente.

    3. En caso de que el código de la moneda sea válido, monstrar en pantalla el nombre completo de la CriptoMoneda.

    4. Solicitar al usuario que ingrese una cantidad de la Cripto Moneda.
    
    5. Conocer su cotización en USD mediante la API de Binance e indicarle al usuario la cantidad en USD que tiene de
       la Cripto Moneda en particular

    AYUDAS:

    1. Documentación de la API CoinMarket:
    https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide

    2. Registrase en: https://coinmarketcap.com/api/ usando el plan Basic que es gratuito.
       Luego de registrase ingresar a https://pro.coinmarketcap.com/account, colocar el ratón sobre la sección 
       API Key (Asteriscos) y dar click en el botón COPY KEY
       pegar la clave en la siguiente sección:
    
    Usar la siguiente clave para las peticiones:
    claveAPI = "clave API generada"
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY' : claveAPI
        }

    3. En el METODO "get" del MODULO "request" de la API de Binance, se solicita la información de de este estilo:
       https://api.binance.com/api/v3/ticker/price?symbol="+moneda+"USDT"

       Donde "moneda" equivale al CODIGO de la Cripto Moneda en cuestion, de esta manera se solicitarán los datos a la
       API de determinada Cripto Moneda, para luego poder manipularlos.

"""

import requests

def valida_name (name):

    """Función que obtendrá el Nombre Completo y real de la Cripto Moneda"""

    claveAPI = "9eae698a-9242-4a25-8769-acd2c4d7a5af"
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY' : claveAPI
        } 

    lista_name = []
    lista_sym = []

    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

    for i in data["data"]:
        lista_name.append(i["name"])
        lista_sym.append(i["symbol"])

    #   Retornando resultados de la función:

    for m in lista_sym:
        if m == name:
            indice = lista_sym.index(m)
            full_name = lista_name[indice]

    return full_name

def valida_cripto(coin):

    """Definición de función que valida si el valor ingresado es válido como Cripto Moneda con la API de Coin Market"""

    claveAPI = "9eae698a-9242-4a25-8769-acd2c4d7a5af"
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY' : claveAPI
        } 

    lista_sym = []

    criptos = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

    for i in criptos["data"]:
        lista_sym.append(i["symbol"])

    if coin in lista_sym:
        return True
    else:
        return False

def valorMoneda(moneda):
    
    """Esta función detecta el valor actual de la Cripto Moneda de acuerdo al día con la API : Binance"""
    
    cripto = requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+moneda+"USDT").json()
    coin = float(cripto['price'])
    return coin

moneda = str(input("Por favor ingrese la moneda que desea ingresar: "))
print("Validando la moneda ingresada...")
while not valida_cripto(moneda):
    moneda = str(input("Moneda INVALIDA, por favor ingrese un nombre válido: "))
    print("Validando la moneda ingresada...")
print("La moneda ingresada es VALIDA")
print("El nombre completo de la CriptoMoneda ingresada es: {}".format(valida_name(moneda)))
qty = float(input("Por favor ingrese una cantidad de la CriptoMoneda {}: ".format(moneda)))
cot = valorMoneda(moneda)
total = cot * qty
print("El valor total de la CriptoMoneda {}, en USD es de: {}".format(moneda, total))