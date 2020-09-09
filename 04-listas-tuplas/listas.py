"""
Listas: son similares a los Arrays, Dinámicas
Tuplas: Fijas valores establecitdos, Estáticas, Son Listas inmutables
Diccionarios: Define una relación uno a uno entre claves y valores.
"""

def run():
    numeros = [1,2,3,4,5]
    numeros.append(6)
    numeros.pop()
    print(numeros)

    paises = ("México", "Colombia", "Argentina")
    print(paises)

    carro = {
        "modelo": 2020,
        "color": "Rojo",
        "marca": "Chevrolet",
        "disponible": True
    }

    print(carro)

    for llave, valor in carro.items():
        print(str(llave) + " - " + str(valor)) 


if __name__ == '__main__':
    run()
