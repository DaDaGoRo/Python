#   Presentación del Programa

print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("Programa que solicita Cinco (5) Cipto Monedas y las muestra en pantalla haciendo uso de 'Listas'")
print("       ")
print("       ")
print("-------       -------")
print("-------       -------")
print("-------       -------")
print("       ")
print("Programa realizado por: DaDa")
print("-------       -------")
print("       ")

#   Declaración de las listas a usar

cripto = ["","","","",""]
cant = [0,0,0,0,0]
precios = [0,0,0,0,0]
total = [0,0,0,0,0]

#   Bucle para pedir nombre de la criptomoneda

for i in range(5):
    cripto[i] = str(input("Por favor ingrese el nombre de la Cripto Moneda {}: ".format(i)))

#   Bucle para pedir la cantidad de la criptomoneda

for i in range(5):
    cant[i] = float(input("Por favor ingrese la cantidad de la Cripto Moneda {}: ".format(i)))

#   Bucle para pedir precios de la criptomoneda

for i in range(5):
    precios[i] = float(input("Por favor ingrese el precio de la Cripto Moneda {}: ".format(i)))

#   Imprimiendo resultados de la Cripto Moneda

print(cripto)
print(cant)
print(precios)

#   Haciendo calculos e imprimiendo

for i in range(5):
    total[i] = cant[i]*precios[i]
    print("El total que tienes en la Cripto Moneda {}".format(cripto[i]),"es de: {}".format(total[i]))

#   Cerrando el programa

print("               ")
print("------- Gracias por usar este programa -------")
print("-------       Hasta la próxima         -------")
print("               ")