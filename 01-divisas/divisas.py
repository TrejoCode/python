"""
Uso básicos de: Casting, If, Inputs, Búcles
"""

menu = """
    Bienvenido al conversor de divisas 💸

    1: Dolar américano
    2: Dolar canadiense
    3: Peso colombiano

    Elige una opción: """

opcion = int(input(menu))


def convertir(nombre_divisa, valor_divisa):
    pesos = input("Escribe la cantidad de pesos mexicanos: ")
    pesos = float(pesos)
    valor_dolar = valor_divisa
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " " + nombre_divisa + " con " + str(pesos) + " pesos mexicanos")

if opcion == 1:

    convertir("Dolares américanos", 21.5)

elif opcion == 2:

    convertir("Dolares canadienses", 16.34)

elif opcion == 3:

    convertir("Pesos colombianos", 172.44)

else:
    print("Opción inválida")