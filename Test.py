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