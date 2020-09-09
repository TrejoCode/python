"""
Verificar si es palíndromo
"""

def verificar(palabra):

    palabra = palabra.replace(' ', '').lower()

    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():

    palabra = input("Escribe una palabra: ")

    if verificar(palabra):
        print("Sí es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()