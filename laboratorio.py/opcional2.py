mujeres_mio = 0
hombres = 0
while True:
    try:
        N = int(input("Ingrese la cantidad de personas a encuestar (N): "))
        if N > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

for i in range(N):
    sexo = int(input("Ingrese el código de sexo (1 para Femenino, 2 para Masculino): "))
    transporte = int(input("Ingrese el código de medio de transporte (1 para MIO, 2 para Vehículo particular, 3 para Bicicleta): "))
    
    if sexo == 1 and transporte == 1:
        mujeres_mio += 1
    if sexo == 2 and transporte == 3:
        hombres += 1

porcentaje_hombres_bicicleta = (hombres / N) * 100

print(f"La cantidad de mujeres que prefieren el MIO es: {mujeres_mio}")
print(f"El porcentaje de hombres que se transportan en bicicleta es: {porcentaje_hombres_bicicleta}%")
mujeres_mio= 0
hombres = 0

while True:
    try:
        N = int(input("Ingrese la cantidad de personas a encuestar (N): "))
        if N > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

for i in range(N):
    sexo = int(input("Ingrese el código de sexo (1 para Femenino, 2 para Masculino): "))
    transporte = int(input("Ingrese el código de medio de transporte (1 para MIO, 2 para Vehículo particular, 3 para Bicicleta): "))
    
    if sexo == 1 and transporte == 1:
        mujeres_mio += 1
    if sexo == 2 and transporte == 3:
        hombres += 1

porcentaje_hombres_bicicleta = (hombres / N) * 100

if __name__ == "__main__":
    print(f"La cantidad de mujeres que prefieren el MIO es: {mujeres_mio}")
    print(f"El porcentaje de hombres que se transportan en bicicleta es: {porcentaje_hombres_bicicleta}%")
















