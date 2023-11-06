secret_number = 92

def mago(variable):
    while(True):
        numero = int(input("Ingrese un numero, entre 0 y 100 : "))
        if(numero == variable):
            print("Ganaste, eres libre")
            break
        else:
            print("Estas atrapado")
            continue
        
if __name__== '__main__':
  mago(secret_number)
    

