#   Se importa el Módulo Request

import requests

#   Copiando la API-KEY de la cuenta que creamos.
#   La cuenta está en: https://coinmarketcap.com/api/
#   El usuario es mi correo
#   El password es: Clave123
#   El código de la API se obtiene de: https://pro.coinmarketcap.com/account/
#   Mi clave de API es: 9eae698a-9242-4a25-8769-acd2c4d7a5af

claveAPI = "9eae698a-9242-4a25-8769-acd2c4d7a5af"
headers = { #   Esto son los parametros que necesitamos pasar en la peticion para que la API nos pueda devolver la información
    'Accepts':'application/json', #   Esto indica que el formato de la respuesta de la API sera JSON, que es un formato legible en Python
    'X-CMC_PRO_API_KEY' : claveAPI #    Aqui indicamos que usaremos la clave de la API que definimos arriba
    } 

#   Inicializaremos una lista vacía para ir almacenando en ella, los valores que vamos enontrando más adelante de las CriptoMonedas

lista = []

#   Usamos la API con los valores que definimos arriba:

criptos = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

#   Para ahora recorreremos el DICCIONARIO que está dentro de otro DICCIONARIO, el cual es "data"
#   Es decir, recorremos uno-a-uno los valores del diccionario que está dentro de la CLAVE criptos["data"] (el cual es otro diccionario)

for i in criptos["data"]:
    lista.append(i["symbol"])


print(type(lista))
print(lista)

#   Comparamos al azar una moneda contra la lista "lista", en este caso "XRP"

valor = "XRP"
if valor in lista:  #   Si coincide el valor, imprimirá "Si"
    print("Si")
else:               #   De lo contrario, imprimirá "No"
    print("No")