#clasificacion de resultados en una competencia
def primo (numero):
    contador = 0 
    for i in range (1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i ==0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    lista = []
    i = int(input("ingrese un numero:"))
    if primo (i):
        print(i,"es primo")
    else:
        pass
    