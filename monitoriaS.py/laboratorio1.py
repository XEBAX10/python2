import random

def operacion (numero):
    global dig1
    global dig2
    global dig3
    global dig4
    global dig5
    dig1 = numero//10000 
    dig2 = (numero//1000)%10
    dig3 = (numero // 100)&10
    dig4 = (numero // 10)&10
    dig5 = numero & 10
    return dig1, dig2, dig3, dig4, dig5


def suma (dig1, dig2, dig3):
    global suma1
    suma1 = dig1 + dig2 + dig3
    return suma1


def suma_2 (dig4, dig5):
    global suma2
    suma2 = dig4 + dig5
    return suma2


def comparacion (suma1, suma2):
    if suma1 == suma2:
        print("la comprobacion es valida")
    else:
        print("La comprobacion es invalida")
    

if __name__=='__main__':

    numero = random.randint(10000,99999)
    print(numero)
    operacion(numero)
    suma (dig1, dig2, dig3)
    suma_2 (dig4, dig5)
    print(comparacion (suma1, suma2))