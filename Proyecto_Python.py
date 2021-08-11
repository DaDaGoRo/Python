#   Importando el módulo de manejo de archivos CSV

import csv

#   Importando el módulo "requests" para usar las API de Binance

import requests

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
    new_info = list()
    new_list = list()
    contador = 0

    #   Abriendo el archivo "Usuarios.csv", en donde se aloja la información de monedas y totales

    lectura = open("Usuarios.csv", "r")
    revisar = csv.reader(lectura, delimiter = ';')

    #   Este bucle busca copiar toda la información del archivo CSV en una lista llamada "new_info"

    for fila in revisar:
        new_info.append(fila)
    lectura.seek(0)     #    Con esta función, devolvemos el índice a la posición inicial
    
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

    #   Pruebas con el usuario 1

    if code_remitente in user1:
        print("Usuario REMITENTE VALIDO - Usuario1 | U1")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for row in revisar:     #   La variable "row" será quien contenga cada FILA dentro del archivo "revisar"
            #   print(row)
            #   print(type(row))    #   Con esto verifiqué que el "class" de "row" es: LIST, por lo que lo puedo trabajar como listas
            if contador == 0:       #   Condicional para ejecutar este código una ÚNICA VEZ
                for indice in row:  #   La variable "indice" será quien contenga cada ELEMENTO de la FILA "row"
                    #   print(indice)
                    #   print(type(indice)) #   Con esto verifiqué que los datos son de tipo "Str" -> Class:str
                    if indice == coin:
                        indice_moneda = int(row.index(indice) + 1)
                        #   print("Indice de la moneda es: {}".format(indice_moneda))
                        #   print(type(indice_moneda))
                        qty_remitente = float(row[indice_moneda])
                        #   print("la cantidad que tiene el remitente es de {}".format(qty_remitente))
                        if qty_remitente >= qty:
                            new_saldo_remitente = qty_remitente - qty
                            row[indice_moneda] = new_saldo_remitente
                            cot = valorMoneda(coin)
                            total = float(row[2])
                            new_total = total - ( cot * new_saldo_remitente )
                            row[2] = new_total
                            new_info.insert(0,row)  #   Con esta sentencia puedo insetar la nueva lista en la primera posición
                            #   Dado que el método "insert", pone la información en el índice indicado, pero NO lo reemplaza
                            #   Es necesario quitar la información "duplicada" de los usuarios, en este caso, U1
                            new_info.pop(1) #   Quito la información del índice "1", pues se corrio la información inicial de posición
                            #   print(type(new_info))
                            #   print(new_info)
                            
                            if code_destino in user2:
                                print("Comprobando la información al DESTINATARIO: Usuario 2 | U2")
                                for info in new_info[1]:    # Seleccionando SOLO la información del Usuario 2 (Índice 1)
                                    #   print(info)         # Con esto comprobé que recorro SOLO la info de Usuario 2
                                    if info == coin:
                                        new_list = new_info[1]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(1,new_list)
                                            new_info.pop(2)
                                            #   print(new_info)     #   Con esto verifiqué que la información estaba correcta
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario1 | U1 y de Usuario2 | U2\n")
                                            print("-------       -------")
                                            print(new_info)
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            break
                                
                                print("Lo sentimos, el Usuario2 | U2 no posee saldo suficiente de la moneda {}".format(coin))
                                break

                            elif code_destino in user3:
                                print("Comprobando la información al DESTINATARIO: Usuario 3 | U3")
                                for info in new_info[2]:    # Seleccionando SOLO la información del Usuario 3 (Índice 2)
                                    if info == coin:
                                        new_list = new_info[2]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(2,new_list)
                                            new_info.pop(3)
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario1 | U1 y de Usuario3 | U3\n")
                                            print("-------       -------")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                
                                print("Lo sentimos, el Usuario3 | U3 no posee saldo suficiente de la moneda {}".format(coin))
                                contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                break
                            
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                            break
                        
                        else:
                            print("Lo sentimos, el Usuario U1 no tiene el saldo suficiente de la moneda {} para hacer la transacción.".format(coin))
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ

        #   Cerremos el archivo de lectura "lectura"
        lectura.close()
    
    #   Pruebas con el usuario 2

    elif code_remitente in user2:
        print("Usuario REMITENTE VALIDO - Usuario2 | U2")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for row in revisar:     #   La variable "row" será quien contenga cada FILA dentro del archivo "revisar"
            if contador == 0:       #   Condicional para ejecutar este código una ÚNICA VEZ
                for indice in row:  #   La variable "indice" será quien contenga cada ELEMENTO de la FILA "row"
                    if indice == coin:
                        indice_moneda = int(row.index(indice) + 1)
                        qty_remitente = float(row[indice_moneda])
                        if qty_remitente >= qty:
                            new_saldo_remitente = qty_remitente - qty
                            row[indice_moneda] = new_saldo_remitente
                            cot = valorMoneda(coin)
                            total = float(row[2])
                            new_total = total - ( cot * new_saldo_remitente )
                            row[2] = new_total
                            new_info.insert(1,row)  #   Con esta sentencia puedo insetar la nueva lista en la segunda posición
                            new_info.pop(2) #   Quito la información del índice "1", pues se corrio la información inicial de posición
                            
                            if code_destino in user1:
                                print("Comprobando la información al DESTINATARIO: Usuario 1 | U1")
                                for info in new_info[0]:    # Seleccionando SOLO la información del Usuario 1 (Índice 0)
                                    if info == coin:
                                        new_list = new_info[0]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(0,new_list)
                                            new_info.pop(1)
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario1 | U1 y de Usuario2 | U2\n")
                                            print("-------       -------")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                
                                print("Lo sentimos, el Usuario1 | U1 no posee saldo suficiente de la moneda {}".format(coin))
                                contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                break

                            elif code_destino in user3:
                                print("Comprobando la información al DESTINATARIO: Usuario 3 | U3")
                                for info in new_info[2]:    # Seleccionando SOLO la información del Usuario 3 (Índice 2)
                                    if info == coin:
                                        new_list = new_info[2]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(2,new_list)
                                            new_info.pop(3)
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario2 | U2 y de Usuario3 | U3\n")
                                            print("-------       -------")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                
                                print("Lo sentimos, el Usuario3 | U3 no posee saldo suficiente de la moneda {}".format(coin))
                                contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                break
                            
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                            break
                        
                        else:
                            print("Lo sentimos, el Usuario U2 no tiene el saldo suficiente de la moneda {} para hacer la transacción.".format(coin))
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ

        #   Cerremos el archivo de lectura "lectura"
        lectura.close()

    #   Pruebas con el Usuario 3

    else:
        print("Usuario REMITENTE VALIDO - Usuario3 | U3")
        print("       ")
        print("Verificando saldo del REMITENTE...")
        for row in revisar:     #   La variable "row" será quien contenga cada FILA dentro del archivo "revisar"
            if contador == 0:       #   Condicional para ejecutar este código una ÚNICA VEZ
                for indice in row:  #   La variable "indice" será quien contenga cada ELEMENTO de la FILA "row"
                    if indice == coin:
                        indice_moneda = int(row.index(indice) + 1)
                        qty_remitente = float(row[indice_moneda])
                        if qty_remitente >= qty:
                            new_saldo_remitente = qty_remitente - qty
                            row[indice_moneda] = new_saldo_remitente
                            cot = valorMoneda(coin)
                            total = float(row[2])
                            new_total = total - ( cot * new_saldo_remitente )
                            row[2] = new_total
                            new_info.insert(2,row)  #   Con esta sentencia puedo insetar la nueva lista en la tercera posición
                            new_info.pop(3) #   Quito la información del índice "1", pues se corrio la información inicial de posición
                            
                            if code_destino in user1:
                                print("Comprobando la información al DESTINATARIO: Usuario 1 | U1")
                                for info in new_info[0]:    # Seleccionando SOLO la información del Usuario 1 (Índice 0)
                                    if info == coin:
                                        new_list = new_info[0]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(0,new_list)
                                            new_info.pop(1)
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario1 | U1 y de Usuario3 | U3\n")
                                            print("-------       -------")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                
                                print("Lo sentimos, el Usuario1 | U1 no posee saldo suficiente de la moneda {}".format(coin))
                                contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                break

                            elif code_destino in user2:
                                print("Comprobando la información al DESTINATARIO: Usuario 2 | U2")
                                for info in new_info[1]:    # Seleccionando SOLO la información del Usuario 2 (Índice 1)
                                    if info == coin:
                                        new_list = new_info[1]
                                        indice_moneda = int(new_list.index(info) + 1)
                                        qty_destino = float(new_list[indice_moneda])
                                        if qty_destino >= qty:
                                            new_saldo_destino = qty_destino + qty
                                            new_list[indice_moneda] = new_saldo_destino
                                            total = float(new_list[2])
                                            new_total = total + ( cot * new_saldo_destino )
                                            new_list[2] = new_total
                                            new_info.insert(1,new_list)
                                            new_info.pop(2)
                                            #   Vamos ahora a cargar el nuevo archivo con los nuevos saldos
                                            users = open("Usuarios.csv", "w", newline ='')
                                            w = csv.writer(users, delimiter = ";")
                                            w.writerows(new_info)   #   Nos aseguramos de pasar la información nueva "new_info"
                                            users.close()
                                            print("Hecho!, hemos actualizado la información de Usuario2 | U2 y de Usuario3 | U3\n")
                                            print("-------       -------")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                        else:
                                            print("No es posible realizar esta transacción")
                                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                            break
                                
                                print("Lo sentimos, el Usuario2 | U2 no posee saldo suficiente de la moneda {}".format(coin))
                                contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                                break
                            
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ
                            break
                        
                        else:
                            print("Lo sentimos, el Usuario U3 no tiene el saldo suficiente de la moneda {} para hacer la transacción.".format(coin))
                            contador = 1    #   Con esto garantizo ejecutar el código una ÚNICA VEZ

        #   Cerremos el archivo de lectura "lectura"
        lectura.close()

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

"""
Usuario1;U1;11432.840999999999;XRP;10.0;BTC;0.3
Usuario2;U2;22457.8664;ETH;10.0;XRP;16.0
Usuario3;U3;86460.81000000001;BTC;0.5;ETH;30.0
XRP U1 - U2 = 9 -> U1: 1 U2: 25
ETH U2 - U3 = 7 -> U2: 3 U3: 37
BTC U3 - U1 = 0.2 -> U3: 0.3 U1: 0.5
"""