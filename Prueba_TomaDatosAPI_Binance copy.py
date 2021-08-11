#   Se importa el Módulo Request

import requests

#   Se utilizar la API de Binance para sacar el valor al día de BitCoin

bc = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()

#   Dado que la API entrega los valor en formato diccionario (dict), entonces ponemos la clave (Key): "prince" que es donde
#   se almance el String con el valor del BitCoin al día, y esto lo asignamos en formato Flotante a la variale "coin"

coin = float(bc['price'])
print(bc, coin)
tipoBc = type(bc)
tipoCoin = type(coin)
print(tipoBc,tipoCoin)

#   Solicitamos la cantidad de la Cripto Moneda y hacemos los cálculos correspondientes para entregar el Total

cant = float(input("Por favor ingrese la cantidad que tiene de la Cripto Moneda: "))
total = coin * cant
print("El total de la Cripto Moneda que tienes es de {}".format(total))