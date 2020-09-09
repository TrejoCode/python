"""
Bucle FOR
continue: Salta el valor
break: Rompe el ciclo, finaliza
"""

def run():

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    for letra in "palabra":
        print(letra)

    for x in range(6):
        print(x)
    else:
        print("Finally finished!")


    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break


if __name__ == '__main__':
    run()