#   Presentación del programa
print("               ")
print("-----     -----")
print("Bienvenido a tu programa de cálculo de la cantidad de Dólares Americanos que tienes en la actualidad")
print("               ")
print("               ")
print("-----     -----")
print("Este programa ha sido desarrollado por: Daniel David Gómez")
print("-----     -----")
print("               ")
print("               ")

#   Solicitud de ingreso del nombre de la Cripto Moneda
NombreCriptoMoneda=input("Ingresa el nombre de la criptomoneda: ")
#   Confirmación del nombre ingresado
print("Gracias, el valor que ingresaste fue: ",NombreCriptoMoneda)

#   Solicitud de ingreso del monto o cantidad que tiene de la Cripto Moneda
MontoCriptoMoneda=float(input("Ingresa ahora el monto (cantidad) que tiene la criptomoneda: "))
#   Confirmación del monto escrito
print("Gracias, el valor ingresado para la cantidad de la ciptomoneda ",NombreCriptoMoneda, " es igual a: ",MontoCriptoMoneda)

#   Solicitud de ingreso del valor de cotización actual de la Cripto Moneda
CotizacionCriptoMoneda=float(input("Gracias por los datos...Finalmente, Ingrese el valor de cotización de la criptomoneda actualente: "))
#   Confirmación de la cotización recibida
print("El valor que ingresaste es: ",CotizacionCriptoMoneda)

#   Haciendo tiempo y realizando calculos...
print("Calculando:.......")
Total=MontoCriptoMoneda*CotizacionCriptoMoneda

#   Entregando resultados
print("El valor total que posees de la CriptoMoneda ",str(NombreCriptoMoneda)," es de: ",Total," Dólares Americanos")
print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")