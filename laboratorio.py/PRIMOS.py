
def esprimo(a):
    for i in range (2, a+1):
        if a%i == 0:
            return False
        else:
            return True

if __name__ == "__main__":

    b = 0
    while b <= 20: 
        a = int(input("Ingrese un numero: "))
        if esprimo(a): 
            print(a, "Es primo")
            b += 1
        else:
            print(a, "No es primo")
    print("Total de primos:", b)
    
    