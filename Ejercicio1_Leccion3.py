#   Presentación del Programa
print("       ")
print("-------       -------")
print("Programa de cálculo de ganancias de la Cripto Moneda por días")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Toma del nombre de la Cripto Moneda
nombreCriptoMoneda=input("Por favor ingrese el nombre de la Cripto Moneda: ")
print("-------       -------")
print("El nombre ingresado fue: ",nombreCriptoMoneda)
print("       ")

#   Toma de la cantidad de la Cripto Moneda
cantidadCriptoMoneda=float(input("Por favor ingrese la cantidad que posee actualmente de la Cripto Moneda: "))
print("-------       -------")
print("       ")

#   Toma de la cantidad de días para la negociación
cantidadDias=int(input("Ingrese la cantidad de días para su negociación de la Cripto Moneda: "))
print("-------       -------")
print("       ")

#   Toma de la ganacia fija por día
gananciaCriptoMoneda=float(input("Por favor ingrese el valor de la ganancia que espera por día de la Cripto Moneda: "))
print("-------       -------")
print("       ")

#   Calculo de resultados
gananciaTotal1=(gananciaCriptoMoneda*cantidadCriptoMoneda)/100
gananciaTotal=gananciaTotal1*cantidadDias
montoTotal=gananciaTotal+cantidadCriptoMoneda
#   Haciendo tiempo...
print("Calculando:...")
print(".......")
print("       ")

#   Mostrando el resultado
print("La CriptoMoneda negociada fue: ",nombreCriptoMoneda)
print("La ganancia total fue de: ",str(gananciaTotal))
print("La cantidad de días negociados fue de: ",str(cantidadDias))
print("               ")
print("El monto total al finalizar el ejercicio fue de: ",str(montoTotal))
print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")