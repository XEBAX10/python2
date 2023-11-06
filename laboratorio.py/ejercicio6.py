#CALCULANDO EL VALOR DE LAS CUOTAS############

def calcularCuoata(prestamo, meses):
    cuotaM= prestamo / meses

    if prestamo <2000000 and meses >=1 and meses <=12:
        cuotaM+= cuotaM * 0.35
    elif prestamo>=2000000 and prestamo <=6000000 and meses >12 and meses <=24:
        cuotaM+=cuotaM * 0.3 
    elif prestamo>6000000 and prestamo <=10000000 and meses >24 and meses <=36:
        cuotaM+=cuotaM * 0.23
    elif prestamo>10000000  and meses >60:
        cuotaM+=cuotaM * 0.1
    else:
        cuotaM+= cuotaM * 0.18
    return cuotaM
    
def valorT (coutaM, meses):
    valorF= coutaM * meses
    return valorF
    
    
if __name__ == '__main__':
    nombre=str(input("ingrese su nombre: "))
    prestamo=int(input("ingrese el valor de su prestamo: "))
    meses=int(input("ingrese la cantidad de meses: "))
    print("nombre: ", nombre)
    cuotaM=calcularCuoata(prestamo, meses)
    coutaF = valorT(cuotaM,meses)
    print("su cuota es: " , cuotaM)
    print("el valor total del prestamos es: ", coutaF)
