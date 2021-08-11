#   Importando el módulo de manejo de archivos CSV

import csv

#   Importando el módulo "requests" para usar las API de Binance

import requests

#   Importación del MÓDULO de fecha y hora del sistema cuando se ejecuta el programa

import datetime

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

#   Procedimiento para imprimir en pantalla el MENÚ de OPCIONES PRINCIPAL DEL PROGRAMA

def menu_principal():

    """ Este procedimiento imprime en pantalla el Menú Principal del Programa """

    print("---------------------")
    print("MENU DE OPCIONES")
    print("---------------------")
    print("       ")
    print("1. Recibir cantidad \n2. Transferir monto \n3. Mostrar balance de una moneda")
    print("4. Mostrar balance general \n5. Mostrar histórico de Transacciones \n6. Salir del Programa")
    print("       ")
    print("-------       -------")
    print("       ")

#   Opción 1: Recibir Cantidad (Este es un procedimiento, y no una función)

def option1():

    """ Este procedimiento nos permitirá realizar las operaciones de la Opción 1 del Menu Principal """
    
    #   Listas conformadas por nombre - código del usuario en particular

    usuarios = ["Usuario1", "U1", "Usuario2", "U2", "Usuario3", "U3"]
    user1 = ["Usuario1", "U1"]
    user2 = ["Usuario2", "U2"]
    user3 = ["Usuario3", "U3"]
    info = list()   #   Esta lista servirá para tener toda la información contenida en el archivo CSV "revisar"
    info_temp = list()  #   Esta lista contrendrá TEMPORALMENTE la información de UN (1) USUARIO A LA VEZ, para ser operado


    #   Abriendo el archivo "Usuarios.csv", en donde se aloja la información de monedas y totales

    lectura = open("Usuarios.csv", "r")
    revisar = csv.reader(lectura, delimiter = ';')  #   "revisar" es de class: "_csv.reader"

    #   Este bucle busca copiar toda la información del archivo CSV en una lista llamada "new_info"

    for fila in revisar:
        info.append(fila)
    #   print(info)     #   Con esto verifiqué que la información si fue pasada con exito a la nueva lista
    lectura.seek(0)     #   Con esta función, devolvemos el índice a la posición inicial
    lectura.close()     #   Con esto cerramos el archivo de forma exitosa (Buenas practicas)
    
    #   Un poco de estética en la presentación del Programa

    print("---------------------")
    print("OPCIÓN 1: RECIBIR CANTIDAD")
    print("---------------------")
    print("       ")

    coin = str(input("Por favor indique el código de la moneda que desea recibir: "))
    print("Validando la moneda ingresada...")
    while not valida_cripto(coin):
        coin = str(input("Moneda NO VALIDA, por favor inténtelo de nuevo: "))
        print("Validando la moneda ingresada...")
    print("       ")
    print("-------       -------")
    print("Moneda VALIDA, el código ingresado es {}".format(coin))
    print("       ")
    qty = float(input("Por favor ingrese la cantidad a recibir de la CriptoMoneda {}: ".format(coin)))
    
    code_remitente = str(input("Por favor ingrese el NOMBRE o CÓDIGO del usuario REMITENTE: "))
    
    while code_remitente not in usuarios:
        code_remitente = str(input("Usuario INVALIDO, por favor inténtelo de nuevo: "))
    
    #   Este bucle, me permmite eliminar el usuario remitente, de la lista de usaurios válidos
    #   de esta manera, el usuario RECEPTOR SIEMPRE es DIFERENTE OBLIGATORIAMENTE del REMITENTE

    for validar in usuarios:
        if validar == code_remitente:
            ind = usuarios.index(validar)
            if len(code_remitente) == 2:
                ind_ = usuarios.index(validar) - 1
            else:
                ind_ = usuarios.index(validar) + 1
            usuarios.pop(ind)
            usuarios.pop(ind_)

    code_destino = str(input("Por favor ingrese el NOMBRE o CÓDIGO del usuario DESTINO: "))
    
    while code_destino not in usuarios:
        code_destino = str(input("Usuario INVALIDO, por favor inténtelo de nuevo: "))
    
    #   Operemos sobre la lista "info", la cual ya tiene la información del archivo CSV
    #   Operaciones sobre el usuario 1 | U1

    if code_remitente in user1:
        print("Usuario REMITENTE VALIDO - Usuario1 | U1")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[0]:
            #   print(indice)   #   Con esto verifiqué efectivamente recorro solo los datos de User1
            info_temp = info[0]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[0][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
            info[0][indice_moneda] = float( qty_remi - qty )
            info[0][2] = float( info[0][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user2:
                print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
                info_temp = info[1]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[1][indice_moneda] )
                        info[1][indice_moneda] = float( qty_dest + qty )
                        info[1][2] = float( info[1][2] ) + ( valorMoneda(coin) * float(info[1][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario1", "Usuario2", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[1][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[1] = info_temp
                    transaccion(coin, "Recepción", "Usuario1", "Usuario2", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
                info_temp = info[2]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[2][indice_moneda] )
                        info[2][indice_moneda] = float( qty_dest + qty )
                        info[2][2] = float( info[2][2] ) + ( valorMoneda(coin) * float(info[2][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario1", "Usuario3", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[2][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[2] = info_temp
                    transaccion(coin, "Recepción", "Usuario1", "Usuario3", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario1 | U1 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Operaciones sobre el usuario 2 | U2

    elif code_remitente in user2:
        print("Usuario REMITENTE VALIDO - Usuario2 | U2")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[1]:
            info_temp = info[1]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[1][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
            info[1][indice_moneda] = float( qty_remi - qty )
            info[1][2] = float( info[1][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user1:
                print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
                info_temp = info[0]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[0][indice_moneda] )
                        info[0][indice_moneda] = float( qty_dest + qty )
                        info[0][2] = float( info[0][2] ) + ( valorMoneda(coin) * float(info[0][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario2", "Usuario1", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[0][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[0] = info_temp
                    transaccion(coin, "Recepción", "Usuario2", "Usuario1", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
                info_temp = info[2]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[2][indice_moneda] )
                        info[2][indice_moneda] = float( qty_dest + qty )
                        info[2][2] = float( info[2][2] ) + ( valorMoneda(coin) * float(info[2][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario2", "Usuario3", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[2][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[2] = info_temp
                    transaccion(coin, "Recepción", "Usuario2", "Usuario3", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario2 | U2 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Operaciones sobre el usuario 3 | U3

    else:
        print("Usuario REMITENTE VALIDO - Usuario3 | U3")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[2]:
            info_temp = info[2]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[2][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
            info[2][indice_moneda] = float( qty_remi - qty )
            info[2][2] = float( info[2][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user1:
                print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
                info_temp = info[0]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[0][indice_moneda] )
                        info[0][indice_moneda] = float( qty_dest + qty )
                        info[0][2] = float( info[0][2] ) + ( valorMoneda(coin) * float(info[0][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario3", "Usuario1", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[0][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[0] = info_temp
                    transaccion(coin, "Recepción", "Usuario3", "Usuario1", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
                info_temp = info[1]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[1][indice_moneda] )
                        info[1][indice_moneda] = float( qty_dest + qty )
                        info[1][2] = float( info[1][2] ) + ( valorMoneda(coin) * float(info[1][indice_moneda]) )
                        transaccion(coin, "Recepción", "Usuario3", "Usuario2", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[1][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[1] = info_temp
                    transaccion(coin, "Recepción", "Usuario3", "Usuario2", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario3 | U3 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Ahora escribiremos el archivo con la nueva información
    users = open("Usuarios.csv", "w", newline ='')
    w = csv.writer(users, delimiter = ";")
    w.writerows(info)
    users.close()

#   Opción 2: Transferir Cantidad (Este es un procedimiento, y no una función)

def option2():

    """ Este procedimiento nos permitirá realizar las operaciones de la Opción 2 del Menu Principal """

    #   Listas conformadas por nombre - código del usuario en particular

    usuarios = ["Usuario1", "U1", "Usuario2", "U2", "Usuario3", "U3"]
    user1 = ["Usuario1", "U1"]
    user2 = ["Usuario2", "U2"]
    user3 = ["Usuario3", "U3"]
    info = list()   #   Esta lista servirá para tener toda la información contenida en el archivo CSV "revisar"
    info_temp = list()  #   Esta lista contrendrá TEMPORALMENTE la información de UN (1) USUARIO A LA VEZ, para ser operado


    #   Abriendo el archivo "Usuarios.csv", en donde se aloja la información de monedas y totales

    lectura = open("Usuarios.csv", "r")
    revisar = csv.reader(lectura, delimiter = ';')  #   "revisar" es de class: "_csv.reader"

    #   Este bucle busca copiar toda la información del archivo CSV en una lista llamada "new_info"

    for fila in revisar:
        info.append(fila)
    #   print(info)     #   Con esto verifiqué que la información si fue pasada con exito a la nueva lista
    lectura.seek(0)     #   Con esta función, devolvemos el índice a la posición inicial
    lectura.close()     #   Con esto cerramos el archivo de forma exitosa (Buenas practicas)
    
    #   Un poco de estética en la presentación del Programa

    print("---------------------")
    print("OPCIÓN 2: TRANSFERIR MONTO")
    print("---------------------")
    print("       ")

    coin = str(input("Por favor indique el código de la moneda que desea enviar: "))
    print("Validando la moneda ingresada...")
    while not valida_cripto(coin):
        coin = str(input("Moneda NO VALIDA, por favor inténtelo de nuevo: "))
        print("Validando la moneda ingresada...")
    print("       ")
    print("-------       -------")
    print("Moneda VALIDA, el código ingresado es {}".format(coin))
    print("       ")
    qty = float(input("Por favor ingrese la cantidad a transferir de la CriptoMoneda {}: ".format(coin)))
    
    code_remitente = str(input("Por favor ingrese el NOMBRE o CÓDIGO del usuario REMITENTE: "))
    
    while code_remitente not in usuarios:
        code_remitente = str(input("Usuario INVALIDO, por favor inténtelo de nuevo: "))
    
    #   Este bucle, me permmite eliminar el usuario remitente, de la lista de usaurios válidos
    #   de esta manera, el usuario RECEPTOR SIEMPRE es DIFERENTE OBLIGATORIAMENTE del REMITENTE

    for validar in usuarios:
        if validar == code_remitente:
            ind = usuarios.index(validar)
            if len(code_remitente) == 2:
                ind_ = usuarios.index(validar) - 1
            else:
                ind_ = usuarios.index(validar) + 1
            usuarios.pop(ind)
            usuarios.pop(ind_)

    code_destino = str(input("Por favor ingrese el NOMBRE o CÓDIGO del usuario DESTINO: "))
    
    while code_destino not in usuarios:
        code_destino = str(input("Usuario INVALIDO, por favor inténtelo de nuevo: "))
    
    #   Operemos sobre la lista "info", la cual ya tiene la información del archivo CSV
    #   Operaciones sobre el usuario 1 | U1

    if code_remitente in user1:
        print("Usuario REMITENTE VALIDO - Usuario1 | U1")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[0]:
            #   print(indice)   #   Con esto verifiqué efectivamente recorro solo los datos de User1
            info_temp = info[0]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[0][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
            info[0][indice_moneda] = float( qty_remi - qty )
            info[0][2] = float( info[0][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user2:
                print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
                info_temp = info[1]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[1][indice_moneda] )
                        info[1][indice_moneda] = float( qty_dest + qty )
                        info[1][2] = float( info[1][2] ) + ( valorMoneda(coin) * float(info[1][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario1", "Usuario2", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[1][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[1] = info_temp
                    transaccion(coin, "Transferencia", "Usuario1", "Usuario2", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
                info_temp = info[2]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[2][indice_moneda] )
                        info[2][indice_moneda] = float( qty_dest + qty )
                        info[2][2] = float( info[2][2] ) + ( valorMoneda(coin) * float(info[2][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario1", "Usuario3", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[2][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[2] = info_temp
                    transaccion(coin, "Transferencia", "Usuario1", "Usuario3", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario1 | U1 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Operaciones sobre el usuario 2 | U2

    elif code_remitente in user2:
        print("Usuario REMITENTE VALIDO - Usuario2 | U2")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[1]:
            info_temp = info[1]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[1][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
            info[1][indice_moneda] = float( qty_remi - qty )
            info[1][2] = float( info[1][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user1:
                print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
                info_temp = info[0]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[0][indice_moneda] )
                        info[0][indice_moneda] = float( qty_dest + qty )
                        info[0][2] = float( info[0][2] ) + ( valorMoneda(coin) * float(info[0][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario2", "Usuario1", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[0][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[0] = info_temp
                    transaccion(coin, "Transferencia", "Usuario2", "Usuario1", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
                info_temp = info[2]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[2][indice_moneda] )
                        info[2][indice_moneda] = float( qty_dest + qty )
                        info[2][2] = float( info[2][2] ) + ( valorMoneda(coin) * float(info[2][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario2", "Usuario3", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[2][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[2] = info_temp
                    transaccion(coin, "Transferencia", "Usuario2", "Usuario3", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario2 | U2 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Operaciones sobre el usuario 3 | U3

    else:
        print("Usuario REMITENTE VALIDO - Usuario3 | U3")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for indice in info[2]:
            info_temp = info[2]
            if coin == indice:
                indice_moneda = int(info_temp.index(indice) + 1)
                qty_remi = float(info[2][indice_moneda])
                break

        if qty_remi >= qty:
            print("Actualizando información del Usuario3 | U3 con los nuevos saldos...")
            info[2][indice_moneda] = float( qty_remi - qty )
            info[2][2] = float( info[2][2] ) - ( valorMoneda(coin) * qty )

            if code_destino in user1:
                print("Actualizando información del Usuario1 | U1 con los nuevos saldos...")
                info_temp = info[0]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[0][indice_moneda] )
                        info[0][indice_moneda] = float( qty_dest + qty )
                        info[0][2] = float( info[0][2] ) + ( valorMoneda(coin) * float(info[0][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario3", "Usuario1", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[0][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[0] = info_temp
                    transaccion(coin, "Transferencia", "Usuario3", "Usuario1", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")
            
            else:
                print("Actualizando información del Usuario2 | U2 con los nuevos saldos...")
                info_temp = info[1]
                for indice in info_temp:
                    if coin == indice:
                        indice_moneda = int( info_temp.index(indice) + 1 )
                        qty_dest = float( info[1][indice_moneda] )
                        info[1][indice_moneda] = float( qty_dest + qty )
                        info[1][2] = float( info[1][2] ) + ( valorMoneda(coin) * float(info[1][indice_moneda]) )
                        transaccion(coin, "Transferencia", "Usuario3", "Usuario2", qty)
                        print("Hecho!, hemos actualizado ambos usuarios")
                        break
                if coin not in info_temp:
                    info_temp[2] = float( info[1][2] ) + ( valorMoneda(coin) * qty)
                    info_temp.append(coin)
                    info_temp.append(qty)
                    info[1] = info_temp
                    transaccion(coin, "Transferencia", "Usuario3", "Usuario2", qty)
                    print("Hecho!, hemos actualizado ambos usuarios")

        else:
            print("Lo sentimos, el Usuario3 | U3 no posee el saldo necesario de la Cripto Moneda: {}".format(coin))
    #   print(info)     #   Con esto comprobé que la información estaba correcta

    #   Ahora escribiremos el archivo con la nueva información
    users = open("Usuarios.csv", "w", newline ='')
    w = csv.writer(users, delimiter = ";")
    w.writerows(info)
    users.close()

#   Opción 3: Mostrar balance de una moneda (Este es un procedimiento, y no una función)

def option3():

    """ Este procedimiento nos permitirá realizar las operaciones de la Opción 3 del Menu Principal """

    #   Un poco de estética en la presentación del Programa

    print("---------------------")
    print("OPCIÓN 3: MOSTRAR BALANCE DE UNA MONEDA")
    print("---------------------")
    print("       ")

    coin = str(input("Por favor ingrese el código de la moneda a mostrar: "))
    print("Validando la moneda ingresada...")
    while not valida_cripto(coin):
        coin = str(input("Moneda NO VALIDA, por favor inténtelo de nuevo: "))
        print("Validando la moneda ingresada...")
    print("       ")
    print("-------       -------")
    print("Moneda VALIDA, el código ingresado es {}".format(coin))
    print("       ")

    #   Validando la cotización actual de la moneda ingresada

    cot = valorMoneda(coin)

    #   Toma de la fecha y hora del sistema de manera Completa
    fechaHoraCompleta=datetime.datetime.now()

    #   Conversión a String de la fecha y hora del sistema

    #   %A establece el formato para el nombre completo del día (Ejemplo: Thursday)
    #   %a establece el formato para el nombre abreviado del día (Ejemplo: Thu - de Thursday)
    #   %d establece el formato para el día en número (Ejemplo: 24)
    #   %D establece el formato para la fecha en formato: 06/24/21 (Mes, día, año en dos dígitos separados por '/')
    #   %B establece el formato para el nombre del Mes(Ejemplo: June)
    #   %m establece el formato para el mes en número (Ejemplo: 06)
    #   %y establece el formato para el año en dos digitos (Ejemplo: 21)
    #   %Y establece el formato para el año con cuatro digitos (Ejemplo: 2021)
    #   %I establece el formato para la hora en formato de 12 horas (Ejemplo: 09:XX:YY)
    #   %M establece el formato para los minutos de la hora (Ejemplo: XX:33:YY)
    #   %S establece el formato para los segundos de la hora (Ejemplo: XX:YY:45)
    #   %s no lo ejecuta - Es ValueError:Invalid format string
    #   %p establece el formato para ver si es AM o PM (Ejemplo: XX.YY:ZZ PM)
    #   %P no lo ejecuta - Es ValueError:Invalid format string

    fechaConFormato=fechaHoraCompleta.strftime("%A %d %B %Y %I:%M:%S %p")

    print("La Cripto Moneda {} tiene una cotización actual de USD $ {}".format(coin, cot))
    print("Esta verificación se realizó el {}".format(fechaConFormato))
    print("-------       -------")
    print("       ")

#   Opción 4: Mostrar Balance General (Este es un procedimiento, y no una función)

def option4():

    """ Este procedimiento nos permitirá realizar las operaciones de la Opción 4 del Menu Principal """

    #   Esta lista servirá para tener toda la información contenida en el archivo CSV "revisar"

    info = list()

    #   Abriendo el archivo "Usuarios.csv", en donde se aloja la información de monedas y totales

    lectura = open("Usuarios.csv", "r")
    revisar = csv.reader(lectura, delimiter = ';')  #   "revisar" es de class: "_csv.reader"

    #   Este bucle busca copiar toda la información del archivo CSV en una lista llamada "new_info"

    for fila in revisar:
        info.append(fila)
    #   print(info)     #   Con esto verifiqué que la información si fue pasada con exito a la nueva lista
    lectura.seek(0)     #   Con esta función, devolvemos el índice a la posición inicial
    lectura.close()     #   Con esto cerramos el archivo de forma exitosa (Buenas practicas)

    #   Toma de la fecha y hora del sistema de manera Completa
    fechaHoraCompleta=datetime.datetime.now()
    fechaConFormato=fechaHoraCompleta.strftime("%A %d %B %Y %I:%M:%S %p")

    #   Un poco de estética en la presentación del Programa

    print("---------------------")
    print("OPCIÓN 4: MOSTRAR BALANCE GENERAL")
    print("---------------------")
    print("       ")
    print("Esta opción nos permite ver el balance general de TODOS LOS USUARIOS registrados")
    print("Esta información está actualizada en la siguiente fecha: {}".format(fechaConFormato))


    #   Vamos a mostrar al información completa de los usuarios

    for i in range(len(info)):
        print("El {}, tiene el código: {}".format(info[i][0], info[i][1]))
        print("El total es USD $ {}".format(info[i][2]))
        print("A continuación se muestra las monedas y cantidades que tiene el usuario:")
        for j in range(3, len(info[i])):
            #   print(info[i][j], end=' ')  #   Con esto comprobé que pude mostrar toda la información, pero ahora toca ordenarla
            print(info[i][j], end='  ')
        print()

#   Opción 5: Mostrar Histórico de Transacciones (Este es un procedimiento, y no una función)

def option5():

    """ Este procedimiento nos permitirá realizar las operaciones de la Opción 5 del Menu Principal """

    #   Abriendo el archivo de las transacciones para realizar la Lectura

    leer = open("Transacciones.csv", "r", newline ='')
    l = csv.reader(leer, delimiter = ";")

    data = list()   #   Variable que contrendrá la información del archivo Transacciones.CSV
    encabezado = ["Fecha y Hora","Moneda","Tipo de Operación","Usuario Remitente","Usuario Destino","Cantidad o Monto"]

    #   Bucle para pasar la información del archivo a la variable

    for row in l:
        data.append(row)
    leer.close()    #   Cerrando el archivo de Transacciones.csv

    #   Un poco de estética en la presentación del Programa

    print("---------------------")
    print("OPCIÓN 5: MOSTRAR HISTÓRICO DE TRANSACCIONES")
    print("---------------------")
    print("       ")
    print("Esta opción nos permite ver TODAS LAS TRANSACCIONES realizadas")

    #   Esta impresión en pantalla muestra el encabezado en distribución correcta de espacios

    print("         {}                            {}           {}       {}        {}        {}".format(encabezado[0], 
    encabezado[1], encabezado[2], encabezado[3], encabezado[4], encabezado[5]))

    #   Este bucle me permite mostrar en pantalla la información contenida en el archivo

    for row in range(len(data)):
        for column in range(len(data[row])):
            print(data[row][column], end='                  ')
        print()
    
    print()
    print("-------       -------")

#   Función de Transacciones: Registrar las Transacciones (Esta SI es una función)

def transaccion( coin, operation, user_rem, user_dest, qty ):

    """ Esta función nos permitirá realizar las operaciones de la Opción 5 del Menu Principal """

    transacciones = list()
    fila = list()

    #   Toma de la fecha y hora del sistema de manera Completa
    fechaHoraCompleta=datetime.datetime.now()
    fechaConFormato=fechaHoraCompleta.strftime("%A %d %B %Y %I:%M:%S %p")
    
    #   Anexando los datos para los históricos de las transacciones a una nueva fila

    fila.append(fechaConFormato)
    fila.append(coin)
    fila.append(operation)
    fila.append(user_rem)
    fila.append(user_dest)
    fila.append(qty)

    #   Anexando la fila nueva a la lista que contiene el histórico

    transacciones.append(fila)

    #   Abriendo el archivo con los históricos para ser editado

    transa = open("Transacciones.csv", "a", newline ='')
    w = csv.writer(transa, delimiter = ";")
    w.writerows(transacciones)
    transa.close()

##################################
#   INICIO LÓGICO DEL PROGRAMA
##################################

#   Presentación del Programa

print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("Programa para el Proyecto Final de Python")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Este programa permite: \n1. Determinar si la moneda está registrada en coinmarket.com")
print("2. Enviar un monto de USD de alguna criptomoneda a un destinatario indicado (identificado por un código)")
print("3. Recibir de un enviador una cantidad de alguna criptomoneda \n4. Consultar el balance de cada una de las CriptoMonedas en USD")
print("5. Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com")
print("6. Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción")
print("7. Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea")
print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Programa realizado por: Daniel David Gómez")
print("El programa solo soporta tres (3) usuarios: Usuario1 - U1, Usuario2 - U2 y Usuario3 - U3")
print("Los demás intentos se verán como NO VALIDOS")
print("       ")
print("-------       -------")
print("       ")

#   Creando la lista con la información de los usuarios válidos
#   Lo considero una lista con tres listas internas, cada una con los datos de 3 usuarios diferentes

user = [
    ["Usuario1", "U1", 0.0],
    ["Usuario2", "U2", 0.0],
    ["Usuario3", "U3", 0.0],
]

#   Creando la Base de Datos de los usuarios en CSV

users = open("Usuarios.csv", "w", newline ='')
w = csv.writer(users, delimiter = ";")
w.writerows(user)
users.close()

#   Creando la Base de Datos de las Transacciones

transa = open("Transacciones.csv", "w", newline ='')
w = csv.writer(transa, delimiter = ";")
transa.close()

#   Agregando información a la LINEA BASE de la Base de Datos

#   Agregando variables para el inicio

follow = 's'                    #   Variable para continuar diligenciando información
user1 = ["Usuario1", "U1"]      #   Listas conformadas por nombre - código del usuario en particular
user2 = ["Usuario2", "U2"]
user3 = ["Usuario3", "U3"]

inicial = str(input("Por favor indique si tiene información que reportar antes de empezar el programa (s / n): "))

while inicial == 's':
    while follow != 'n':

        usuario = str(input("Por favor ingrese el nombre o código del usuario que quiere actualizar: "))
        if usuario in user1:
            moneda = str(input("Por favor ingrese la moneda que desea ingresar: "))
            print("Validando la moneda ingresada...")
            while not valida_cripto(moneda):
                moneda = str(input("Moneda INVALIDA, por favor ingrese un nombre válido: "))
                print("Validando la moneda ingresada...")
            print("La moneda ingresada es VALIDA")
            cantidad = float(input("Por favor ingrese la cantidad que posee de la CriptoMoneda: "))
            cot = valorMoneda(moneda)
            user[0].append(moneda)
            user[0].append(cantidad)
            usd = cot * cantidad
            total = user[0][2]
            total = total + usd
            user[0][2] = total
            transaccion(moneda, "Carga", "Carga", "Usuario1", cantidad)
            follow = str(input("Deseas agregar más información? (s / n): "))
        elif usuario in user2:
            moneda = str(input("Por favor ingrese la moneda que desea ingresar: "))
            print("Validando la moneda ingresada...")
            while not valida_cripto(moneda):
                moneda = str(input("Moneda INVALIDA, por favor ingrese un nombre válido: "))
                print("Validando la moneda ingresada...")
            print("La moneda ingresada es VALIDA")
            cantidad = float(input("Por favor ingrese la cantidad que posee de la CriptoMoneda: "))
            cot = valorMoneda(moneda)
            user[1].append(moneda)
            user[1].append(cantidad)
            usd = cot * cantidad
            total = user[1][2]
            total = total + usd
            user[1][2] = total
            transaccion(moneda, "Carga", "Carga", "Usuario2", cantidad)
            follow = str(input("Deseas agregar más información? (s / n): "))
        elif usuario in user3:
            moneda = str(input("Por favor ingrese la moneda que desea ingresar: "))
            print("Validando la moneda ingresada...")
            while not valida_cripto(moneda):
                moneda = str(input("Moneda INVALIDA, por favor ingrese un nombre válido: "))
                print("Validando la moneda ingresada...")
            print("La moneda ingresada es VALIDA")
            cantidad = float(input("Por favor ingrese la cantidad que posee de la CriptoMoneda: "))
            cot = valorMoneda(moneda)
            user[2].append(moneda)
            user[2].append(cantidad)
            usd = cot * cantidad
            total = user[2][2]
            total = total + usd
            user[2][2] = total
            transaccion(moneda, "Carga", "Carga", "Usuario1", cantidad)
            follow = str(input("Deseas agregar más información? (s / n): "))
        else:
            print("Usuario NO VALIDO, por favor intentelo de nuevo.")
    
    else:
        users = open("Usuarios.csv", "w", newline ='')
        w = csv.writer(users, delimiter = ";")
        w.writerows(user)
        users.close()
        inicial = 'n'
else:
    print("       ")
    print("-------       -------")
    print("Ok, empecemos con el programa")
    print("-------       -------")
    print("       ")
    follow = 'r'    #   Cambio el valor de la variable para que sea compatible con las nuevas sentencias
    choose = ''     #   Inicializo la varible de tipo 'Str' y vacía

#   Luego de obtener la Línea Base del programa, debemos imprimir el Menú de Opciones del Programa

menu_principal()

while choose != '6':

    while follow != 's':

        #   La variable "choose" será la selección del menú
        choose = str(input("Digite por favor la opción que quiere tomar: "))
        print("La opción seleccionada es {}".format(choose))
        if choose == '1':
            option1()
        elif choose == '2':
            option2()
        elif choose == '3':
            option3()
        elif choose == '4':
            option4()
        elif choose == '5':
            option5()
        elif choose == '6':
            break
        follow = str(input("Desea realizar salir del programa (s) o regresar el menú anterior (r)?: "))
        if follow == 's':
            break
        elif follow == 'r':
            print("       ")
            print("-------       -------")
            menu_principal()
        else:
            print("Opción INCORRECTA, por favor seleccione una de las opciones dadas")
            print("       ")
            print("-------       -------")
            menu_principal()
    
    else:
        choose = '6'
        print("       ")
        print("-------       -------")
        print("Has seleccionado la opción de SALIR, gracias por usar este programa...Hasta pronto!")
        print("-------       -------")
        print("       ")
        break

else:
    print("       ")
    print("-------       -------")
    print("Has seleccionado la opción de SALIR, gracias por usar este programa...Hasta pronto!")
    print("-------       -------")
    print("       ")
    exit