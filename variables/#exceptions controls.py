#exceptions controls
# dividendo=1
# divisor=0
# try:
#    result= dividendo/divisor
# except ZeroDivisionError:
#    print("can't dvide by zero")
# else:
#    print("it didn't divide by zero")
# finally:
#    print("america de cali ")

#print(result

# try:
#     global value
#     value = int(input('Ingresa un número natural: '))
# #print('El recíproco de', value, 'es', 1/value)        
# except ValueError:
#     print("Type your value correct, enter")
# else:
#     print("Data correct")

try:
    numero = int(input("ingrese un numero: "))
except Exception: #padre de la excepciones, si no conozco el tipo de exepcion puedo poner esta...
    print("numero invalido")

##########

try:
    numero = int(input("ingrese un numero: "))
except Exception as errorRandom: #descirpcion del eror
    print("numero invalido")

#########
import logging

try:
    numero = int(input("ingrese un numero: "))
except Exception as errorRandom: #descirpcion mas detallada del error
    loggin.exception("el eror es el siguiente")