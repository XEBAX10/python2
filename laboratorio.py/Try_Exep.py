# try:
#  print(10/"X")
# except Exception as e :
#  print("error en el sistema: ", e )


# try:
#  print(10/0)
# except TypeError as e :
#  print("error en el sistema - tipo: ", e )
# except ZeroDivisionError as ex :
#  print("error en el sistema: - division ", ex )
# finally:
#  print("carechimba escriba lo que es HPPPP")
 
# try:
#     numero= int(input("introduce un numero: "))
#     numero2= int(input("introduce otro numero: "))
#     resultado= numero + numero2
#     print(resultado)
# except:
#     print("debe introducir un hp numero, no letras pendejo...")
# finally:
#     print("si o si ")

#CONTROL DE EXCEPCIONES CON BUCLE WHILE:
while(True):
    try:
        numero= int(input("introduce un numero: "))
        numero2= int(input("introduce otro numero: "))
        resultado= numero + numero2
        print(resultado)
        break
    except:
        print("debes introducir un numero vuelve a intentarlo...")