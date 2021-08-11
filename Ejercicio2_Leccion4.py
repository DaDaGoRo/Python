#   Presentación del Programa

print("       ")
print("-------       -------")
print("Programa de cálculo de acumulado en Dólares de la Cripto Moneda y Fecha de la transacción")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Solicitud del nnombre de la Cripto Moneda

nombreCriptoMoneda=input("Por favor ingresa el nombre de la Cripto Moneda: ")
print("Vale, el nombre de la criptomoneda que ingresaste es: ",nombreCriptoMoneda)

#   Solicitud de la cantidad acumulada que se tiene de la Cripto Moneda

acumuladoCriptoMoneda=float(input("Por favor ingresa la cantidad acumulada que tienes de esta Cripto Moneda ------> "))
strAcumuladoCM=str(acumuladoCriptoMoneda)
print("Vale, has indicado que tienes la cantidad ",strAcumuladoCM,"de la Cripto Moneda ",nombreCriptoMoneda)

#   Solicitud de la cotización del día de la Cripto Moneda

cotizacionCriptoMoneda=float(input("Por favor indicanos el valor de la cotización a día de hoy de la Cripto Moneda: "))
strCotizacionCM=str(cotizacionCriptoMoneda)
print("De acuerdo, has indicado que el valor de la cotización de la Cripto Moneda ",nombreCriptoMoneda,"es de: ",strCotizacionCM)

#   Importación del MÓDULO de fecha y hora del sistema cuando se ejecuta el programa

import datetime

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

#   Estableciendo la fecha futura (en 8 días)

fechaDelta=datetime.timedelta(days=7)
fechaHoraFutura=fechaHoraCompleta+fechaDelta
fechaConFormatoFutura=fechaHoraFutura.strftime("%A %d %B %Y %I:%M:%S %p")

#   Calculando datos de la ciptomoneda e imprimiendo resultados

cantidadTotalHoy=acumuladoCriptoMoneda*cotizacionCriptoMoneda
ganancias=cantidadTotalHoy*0.05*7
cantidadTotal=cantidadTotalHoy+ganancias
print("El total de Dólares que tienes con la Cripto Moneda ",nombreCriptoMoneda,"es de: ",str(cantidadTotalHoy))
print("La fecha y hora de esta transacción fue: ",fechaConFormato)
print("Finalmente, con un crecimiento del 5% por día, para la fecha: ",fechaConFormatoFutura,"tendrás un total de: ",str(cantidadTotal))

#   Cerrando el programa

print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")